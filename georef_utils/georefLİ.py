import os
import numpy as np
from osgeo import gdal, ogr, osr
import uuid
import glob 

#Add georefrence!! 
mimic_dir = r"C:\Users\PROCOMP11-PC\Desktop\Görüntüler\Sariyer\SARIYER\PAN\tif"
girdi_dir = r"C:\Users\PROCOMP11-PC\Desktop\Görüntüler\Sariyer\sariyerrr"

mimic = glob.glob(mimic_dir + "\*.tif")
girdi = glob.glob(girdi_dir + "\*.tif")


out_dir = r"C:/Users/PROCOMP11-PC/Desktop/Görüntüler/Sariyer/sariyerr_merge/" #where to save #Dikkat et.


for i,(mimik,girti) in enumerate(zip(mimic,girdi)):
    #open
    ds = gdal.Open(girti)
    arrayRaster = ds.ReadAsArray()

    red   = arrayRaster[0]
    green = arrayRaster[1]
    blue  = arrayRaster[2]

    cols = ds.RasterXSize
    rows = ds.RasterYSize

    driver = gdal.GetDriverByName('GTiff')
    run_ID = str(uuid.uuid4())

    outRasterDir = out_dir + 'geo-referenced-' + run_ID + '.tif' #Where to save 

    print("[INFO]: {}. patch is processing...".format(i + 1),outRasterDir)
    outRaster = driver.Create(outRasterDir, cols, rows, 3, gdal.GDT_Byte)

    #get the internal info
    mimik_ds = gdal.Open(mimik)

    #projection and geo-transformation
    outRaster.SetGeoTransform(mimik_ds.GetGeoTransform())
    outRaster.SetProjection(mimik_ds.GetProjection())

    outbandRed = outRaster.GetRasterBand(1)
    outbandRed.WriteArray(red)
    outbandRed = outRaster.GetRasterBand(2)
    outbandRed.WriteArray(green)
    outbandRed = outRaster.GetRasterBand(3)
    outbandRed.WriteArray(blue)

    #outRaster.FlushCache() 

    del ds
    del mimik_ds
