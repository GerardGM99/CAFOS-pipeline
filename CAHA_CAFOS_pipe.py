# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 19:56:11 2024

@author: Gerard Garcia
"""

import os
from pathlib import Path
import calibration as calib

# Set directories as a global variable
# DATADIR = input('Input directory where your data are: ')
# directory = Path(DATADIR)
# PLOTDIR = os.path.join(DATADIR, "plots")

calib.init()

def general_calibrations():
    print('*************************')
    print('MASTER BIAS')
    print('*************************')
    calib.apply_master_bias(img_code='caf*', plot=False)
    print('Master BIAS applied')
    
    print('*************************')
    print('MASTER FLAT')
    print('*************************')
    calib.apply_master_flat(plot = False)
    print('Master FLAT applied')
    
    print('*************************')
    print('WAVELENGHT CALIBRATIONS')
    print('*************************')
    calib.wavelength_calibration(plot=False)

def science():
    print('*************************')
    print('SKY SUBTRACTION')
    print('*************************')
    calib.sky_substraction()
    
    print('*************************')
    print('ALIGNMENT')
    print('*************************')
    x_min, x_max, y_min, y_max = calib.spec_align()
    
    print('*************************')
    print('SPECTRUM EXTRACTION')
    print('*************************')
    calib.spec_extract(x_min, x_max, y_min, y_max)
    
    print('*************************')
    print('FLUX CALIBRATION')
    print('*************************')
    flux_cal = input('Apply flux calibration? (Chose "yes" or "no")')
    if flux_cal in ['Yes', 'yes', 'Y', 'y']:
        calib.flux_calib()
