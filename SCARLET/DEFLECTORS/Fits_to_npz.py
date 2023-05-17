#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:48:36 2023

@author: nandinisahu
"""
from astropy.io import fits
import numpy as np

fits_file='E:/UNSW/HONOURS/GRAVITATIONAL LENSING/SCARLET/DEFLECTORS/AGEL002527+101107/fits images/legacysurvey-0064p102-image-g_extn=1_POS=6.3642,10.1853_SIZE=0.1,0.1.fits'

infile=fits.open(fits_file)

img_data=infile[0].data
header=infile[0].header

#convert to npz
np.savez_compressed('E:/UNSW/HONOURS/GRAVITATIONAL LENSING/SCARLET/DEFLECTORS/AGEL002527+101107/fits images/legacysurvey-0064p102-image-g_extn=1_POS=6.3642,10.1853_SIZE=0.1,0.1.fits_test', img_data=img_data, header=header)

#load npz
npz_file_load = np.load('E:/UNSW/HONOURS/GRAVITATIONAL LENSING/SCARLET/DEFLECTORS/AGEL002527+101107/fits images/legacysurvey-0064p102-image-g_extn=1_POS=6.3642,10.1853_SIZE=0.1,0.1.fits_test.npz')

#checks
print(npz_file_load.files)
print(npz_file_load['img_data'])
print(npz_file_load['header'])