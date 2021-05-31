import numpy as np
import matplotlib.pyplot as plt
import subprocess, glob
from osgeo import gdal
import os
#Merge multiple tiles together!

os.chdir(r"C:\Users\PROCOMP11-PC\Desktop\Görüntüler\Sariyer\sariyerr_geo")
source_dir = r"C:\Users\PROCOMP11-PC\Desktop\Görüntüler\Sariyer\sariyerr_merge"

extension = 'tif'

georef_images = glob.glob(source_dir + "\*.{}".format(extension))

print("[INFO]: There are {} images to merge..".format(len(georef_images)))

files_string = " ".join(georef_images)
command = "python C:\\Users\\PROCOMP11-PC\\Anaconda3\\Lib\\site-packages\\osgeo\\scripts\\gdal_merge.py -o PanColorGAN_Output_SARIYER_SON.tif -of gtiff +" + files_string
output = subprocess.check_output(command)
output