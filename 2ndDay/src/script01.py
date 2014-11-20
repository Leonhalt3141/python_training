# -*- coding: utf-8 -*-
# script01.py
# 2014.11.20 K. Kuwata

from image import landsat


# Calculating reflectance of Band3
limage = landsat("/Users/ken/Data/Landsat/LE71070352000329EDC00_B3.TIF", "/Users/ken/Data/Landsat/LE71070352000329EDC00_MTL.txt", 7, 3)

 # Get pixel data as array
array = limage.Band2Array()
 # Get information from a parameter file
Parameters = limage.ReturnParameters()
 # Calculate Radiance from DN
Radiance = limage.DN2Radiance(array, Parameters)
 # Calculate Reflectance from Radiance
Reflectance3 = limage.Radiance2Reflectance(Radiance, Parameters)
 # Make a Geotiff file
limage.WriteArrayAsImage("Reflectance_B3.tif", Reflectance3)

# Calculating reflectance of Band4
limage = landsat("/Users/ken/Data/Landsat/LE71070352000329EDC00_B4.TIF", "/Users/ken/Data/Landsat/LE71070352000329EDC00_MTL.txt", 7, 4)

 # Get pixel data as array
array = limage.Band2Array()
 # Get information from a parameter file
Parameters = limage.ReturnParameters()
 # Calculate Radiance from DN
Radiance = limage.DN2Radiance(array, Parameters)
 # Calculate Reflectance from Radiance
Reflectance4 = limage.Radiance2Reflectance(Radiance, Parameters)

# Calculating NDVI
 # Get a pixel column number
cols = limage.iminfo['cols']
 # Get pixel row number
rows = limage.iminfo['rows']

 # Calculate NDVI
NDVI = limage.CalcNDVI(NIR=Reflectance4.reshape(cols * rows), Red=Reflectance3.reshape(cols * rows))

 # Make a Geotiff file
limage.WriteArrayAsImage("NDVI.tif", NDVI.reshape(rows, cols))
