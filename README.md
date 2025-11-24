# GEOM7001-LST-UHII
University assignment: Python processing workflow to derive LST and UHII from Landsat 8 Level-1 scenes using radiative transfer and amtospheric modelling. Includes daytime and nighttime scenes. 

# Intro
I'm not a coder first and foremost, so please don't judge my code too harshly. It got a little messy at the end with the time crunch.  

Essentially, the issue I had to solve was having lots of processing, without bloating up the storage space. I could've streamed the data in hindsight but I was a little worried at the time about lack of funding to my data source and thereby losing access.  

To solve the issue, I mainly generate VRTs through python, which are essentially just an XML format. So the large majority of my preprocessing is just glorified text generation. I just use input the required parameters into templates.
