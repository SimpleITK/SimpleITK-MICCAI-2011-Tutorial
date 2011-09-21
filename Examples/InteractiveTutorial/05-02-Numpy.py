# Welcome to the Interactive Tutorial
print 'SimpleITK Interactive Tutorial'

# Every demo starts by importing the SimpleITK module
import SimpleITK as sitk
import numpy as np

# <demo> stop
import os
dataDir = os.environ["HOME"] + "/SimpleITK-MICCAI-2011-Tutorial"
image = sitk.ReadImage ( dataDir + "/iasem-cells.nrrd" )

# <demo> stop

a = sitk.GetArrayFromImage( image )


# carefully choosen bin so that the index is the value for uint8
h, bins = np.histogram( a, bins=255, range=(0,255) )

# <demo> stop

mode = 0
for i in range(1, h.shape[0] ):
    if( h[i] > h[mode] ):
        mode = i

print "Mode of image: " + str( mode )

# <demo> stop
