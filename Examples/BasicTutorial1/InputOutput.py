# Welcome to the Input/Output demo
print 'SimpleITK Input Output'

# <demo> --- stop ---

# Every demo starts by importing the SimpleITK module
import SimpleITK as sitk

# <demo> --- stop ---

# Find some data
import os
dataDir = os.environ["HOME"] + "/src/SimpleITK/Testing/Data/Input"

# <demo> --- stop ---

# Create a reader
reader = sitk.ImageFileReader()
reader.SetFileName ( dataDir + "/WhiteDots.png" )
# Read
image = reader.Execute()

# <demo> --- stop ---

# meh, do it with less typing
image = sitk.ReadImage ( dataDir + "/WhiteDots.png" )

# <demo> --- stop ---

# What'd we get?
print image

# <demo> --- stop ---

# What's the image look like?
sitk.Show ( image )

# <demo> --- stop ---

# 3D image
image = sitk.ReadImage ( dataDir + "/OAS1_0001_MR1_mpr-1_anon.nrrd" )
sitk.Show ( image )

# <demo> --- stop ---

# Output, set ITK for valid output formats
sitk.WriteImage ( image, "/home/tutorial/Example.nii" )

# And go load it into ImageJ/Fiji
