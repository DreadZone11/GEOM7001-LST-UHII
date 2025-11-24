# GEOM7001-LST-UHII
University assignment: Python processing workflow to derive LST and UHII from Landsat 8 Level-1 scenes using radiative transfer and amtospheric modelling. Includes daytime and nighttime scenes. 

# Intro
I'm not a coder first and foremost, so please don't judge my code too harshly. It got a little messy with the time crunch at the end. As such, a lot of the later code remains uncommented.

Essentially, the issue I had to solve was that I had to generate a lot of parameters to derive LST from Landsat 8/9 Level-1 Digital Numbers (i.e Emissivity, TOA Radiance, TOA Brightness, Surface Reflectance, NDVI, NDWI, NDBI, etc.). I had to do this in a way that was not going to blow up my storage. Obviously, I could've streamed the data, but I was a little worred about losing access to my data source at the time, due to funding cuts.

To solve the issue, I mainly generate Virtual Raster Tables (VRTs) through Python notebooks. VRTs allow you to apply a Python pixel function, which determines the value of the pixel based on the pixel function. VRTs are essentially an XML text file, so the large majority of my processing is just glorified text generation. I simply use templates to input the required parameters.

# Main Contents:
- [Data Selection](00_data_select.ipynb)
  - [Bounding Box](bbox_sm.gpkg)
- [Searches](00_searches.md)
  - [Search Results - Daytime](00_search_d.csv) (Note: the number of returns has changed using the same criteria; 11 -> 8 [24/11/2025])
  - [Search Results - Nighttime](00_search_n.csv)
- [Processing and LST Derivation](01_processing.ipynb)
- [Compositing and Mosaicking](02_composite.ipynb)
- [UHI Derivation](03_uhi.ipynb)
  - [Urban Shapefile](urban.gpkg)
- [LCZ Analysis](04_lcz.ipynb)
- [Validation](05_validation.ipynb)
- [Outputs](out/)

# Additional:
- [libRadtran Templates](libradtran/templates)
- [Pixel Functions](pixel_functions)
- [VRT Templates](templates)

# Not Included:
- Original Landsat 8 data (for obvious size reasons)

# Usage:
If you want to test, I used the following folder structure. It might work otherwise, seeing as the code searches folders recursively for Landsat data. Otherwise, the code might need tweaking.

- data
  - LANDSAT
    - LC08_LT1P_{PATH}{ROW}_{DATE}
      - LC08_LT1P_{PATH}{ROW}_{DATE}_B10.tif
      - LC08_LT1P_{PATH}{ROW}_{DATE}_B11.tif
      - LC08_LT1P_{PATH}{ROW}_{DATE}_MTL.txt
      - LC08_LT1P_{PATH}{ROW}_{DATE}_QA_PIXEL.tif
      - ...
