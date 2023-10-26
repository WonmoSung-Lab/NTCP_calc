import matplotlib.pyplot as plt
from ImgProcessing import ImgProcessing

fin = "/Volumes/data-1/ksh/pelvic_RIL/raw_data/1/ct/"

i = ImgProcessing()
i.dcm2nii(fin)
ct_arr = i.ct_arr
ct = i.ct_nii

mask_fin = "/Volumes/data-1/ksh/pelvic_RIL/raw_data/1/contour/2.16.840.1.114362.1.12148098.22261327066.644512811.711.5147.dcm"
i.mask2arr(ct,mask_fin,'liver')
mask_arr = i.mask_arr

fig, ax = plt.subplots(1,2)

ax[0].matshow(ct_arr[:,250,:])
ax[1].matshow(mask_arr[:,250,:])
plt.show()

