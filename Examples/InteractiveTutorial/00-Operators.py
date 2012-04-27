# Welcome to the Interactive Tutorial
print 'SimpleITK Interactive Tutorial'

# <demo> auto

# Every demo starts by importing the SimpleITK module
import SimpleITK as sitk

# <demo> stop
import os
dataDir = os.environ["HOME"] + "/src/SimpleITK/Testing/Data/Input"
image = sitk.ReadImage ( dataDir + "/RA-Slice-Short.nrrd" )
sitk.Show ( image, "Slice" )

# <demo> stop

# Add to the image
sitk.Show ( 100 + image, "SlicePlus100" )

# <demo> stop

# Create 2 floating point images
xImg = sitk.Image( 256, 256, sitk.sitkFloat32 )
yImg = sitk.Image( 256, 256, sitk.sitkFloat32 )

# <demo> stop

# Loop over all the voxels
for y in range( 0, xImg.GetSize()[1] ):
    for x in range( 0, xImg.GetSize()[0] ):
        # Note two ways to set pixels
        xImg.SetPixel( x, y, x )
        yImg[x, y] = y

sitk.Show ( xImg, "XImage" )
sitk.Show ( yImg, "YImage" )
# <demo> stop

# Construct a gaussian
sigma = 50

xImg = sitk.SubtractConstantFrom( xImg,  xImg.GetSize()[0] / 2 )
yImg = yImg - yImg.GetSize()[1] / 2

gaussianImg = sitk.Exp( -1 * (xImg**2 + yImg**2) / (2.0 * sigma**2) )
sitk.Show ( gaussianImg, "GaussianImage" )

# <demo> stop

# Other Image Operator demos?
