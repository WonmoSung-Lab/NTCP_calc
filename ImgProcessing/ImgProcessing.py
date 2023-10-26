import SimpleITK as sitk
import pydicom as pdcm
import numpy as np
import cv2
import os

class ImgProcessing:
    __slots__ = ["ct_arr","ct_nii","mask_arr","mask_nii"]
    def __init__(self):
        self.ct_arr = {}
        self.ct_nii = {}
        self.mask_arr = {}
        self.mask_nii = {}

    def dcm2nii(self,dcm_path,write_img=False,output_fin='converted_ct.nii'):

        if os.path.isdir(dcm_path):
            if dcm_path[-1] != '/':
                dcm_path = dcm_path + '/'

            list_fin = os.listdir(dcm_path)
            list_fin = [fin for fin in list_fin if not fin.startswith('.')]

            ct_stack = []
            for i in sorted(list_fin):
                dcm = pdcm.read_file(dcm_path + i)
                s = int(dcm.RescaleSlope)
                b = int(dcm.RescaleIntercept)
                arr = s * dcm.pixel_array + b
                ct_stack.append(np.squeeze(arr))
            ct_arr = np.array(ct_stack)
            self.ct_arr = np.flip(ct_arr, axis=0)
            print(f"folder:{dcm_path} is successfully converted")

            dir = np.array(dcm.ImageOrientationPatient)
            dir = np.append(dir, (0, 0, 1))
            ori = dcm.ImagePositionPatient
            spac = [dcm.PixelSpacing[0], dcm.PixelSpacing[1], dcm.SliceThickness]
            self.ct_nii = sitk.GetImageFromArray(self.ct_arr)
            self.ct_nii.SetDirection(dir)
            self.ct_nii.SetOrigin(ori)
            self.ct_nii.SetSpacing(spac)

            if write_img == True:
                sitk.WriteImage(self.ct_nii, output_fin)
                print(f"Image was saved as {output_fin}")
        else:
            raise FileExistsError (f"{dcm_path} is not a directory")


    def mask2arr(self,ct_nii, rtst_fin, organ_name,write_img=False,output_fin='extracted_mask.nii'):
        origin = np.array(ct_nii.GetOrigin())
        spacing = np.array(ct_nii.GetSpacing())
        direction = np.array(ct_nii.GetDirection())
        arr = np.zeros_like(sitk.GetArrayFromImage(ct_nii))
        dcm = pdcm.dcmread(rtst_fin)

        mask_point = []
        for i in dcm.StructureSetROISequence:
            if i.ROIName.lower() == organ_name.lower():
                num = i.ROINumber
                for j in dcm.ROIContourSequence:
                    if j.ReferencedROINumber == num:
                        k = j.ContourSequence
                        for l in k:
                            mask_point.append(l.ContourData)
        reshaped_point = []
        for coords in mask_point:
            reshaped_point.append(np.reshape(coords, [len(coords) // 3, 3]))
        for slice_num in range(len(reshaped_point)):
            point = []
            for point_num in range(len(reshaped_point[slice_num])):
                reshaped_point[slice_num][point_num] = (reshaped_point[slice_num][point_num] - origin) / spacing
                point.append(reshaped_point[slice_num][point_num][:2])
            point = np.around(np.array(point, dtype=np.int32))
            z = np.int32(reshaped_point[slice_num][point_num][2])
            cv2.fillPoly(img=arr[z, :, :], pts=[point], color=1)
        self.mask_arr = arr
        print(f"Image was successfully extracted")

        if write_img:
            self.mask_nii = sitk.GetArrayFromImage(self.mask_arr)
            self.mask_nii.SetDirection(direction)
            self.mask_nii.SetOrigin(origin)
            self.mask_nii.SetSpacing(spacing)
            sitk.WriteImage(self.mask_nii,output_fin)
            print(f"Image was saved as {output_fin}")





