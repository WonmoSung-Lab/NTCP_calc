'''Instruction on image processing class
    Using nifti format is recommended for convenience of handling files'''
from ImgProcessing import ImgProcessing

fin = "/Volumes/data-1/ksh/pelvic_RIL/raw_data/1/ct/"
mask_fin = "/Volumes/data-1/ksh/pelvic_RIL/raw_data/1/contour/2.16.840.1.114362.1.12148098.22261327066.644512811.711.5147.dcm"

i = ImgProcessing()
i.dcm2nii(fin)                          #adjust default: write_img = False, output_fin = 'converted_ct.nii'
ct_arr = i.ct_arr
ct_nii = i.ct_nii

i.mask2arr(ct_nii,mask_fin,'liver')     #adjust default: write_img = False, output_fin = 'extracted_mask.nii'
mask_arr = i.mask_arr
mask_nii = i.mask_nii

'''structure mask plot'''
import matplotlib.pyplot as plt
import numpy as np

ct_arr = np.flip(ct_arr)
mask_arr = np.flip(mask_arr)

fig, ax = plt.subplots(1,2)
ax[0].matshow(ct_arr[:,250,:])
ax[1].matshow(mask_arr[:,250,:])
plt.savefig("liver_mask.png",dpi=200)
plt.show()

