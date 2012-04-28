# Welcome to the Morphology demo
print 'SimpleITK Morphology'

# Every demo starts by importing the SimpleITK module
import SimpleITK as sitk

# Find some data
import os
dataDir = os.environ["HOME"] + "/src/SimpleITK/Testing/Data/Input"
image = sitk.ReadImage ( dataDir + "/WhiteDots.png" )
# Convert to 0 and 1, if you can't see it, check window/level!
image = sitk.BinaryThreshold ( image, 0, 256, 0, 1 )
sitk.Show ( image, "WhiteDots" )

# <demo> --- stop ---

# Erode, not to exciting, did something happen?
sitk.Show ( sitk.BinaryErode ( image ), "Eroded" )

# <demo> --- stop ---

# Hmm, can we visualize better?  Zoom in to see...
# Use pixel-wise operators
sitk.Show ( 127 * image + 127 * sitk.BinaryErode ( image ), "ThinErosion" )

# <demo> --- stop ---

sitk.Hash ( image + 2 )
sitk.Hash ( sitk.AddConstantTo ( image, 2 ) )

sitk.Hash ( image * 2 )
sitk.Hash ( sitk.MultiplyByConstant ( image, 2 ) )

# <demo> --- stop ---

# Bigger kernel
filter = sitk.BinaryErodeImageFilter()
filter.SetKernelRadius ( 5 ).SetForegroundValue ( 1 )
eroded = filter.Execute ( image )
sitk.Show ( 127 * image + 127 * eroded, "ThickErosion" )

# <demo> --- stop ---

# Bigger kernal with a cross
filter.SetKernelType ( sitk.BinaryErodeImageFilter.Cross )
eroded = filter.Execute ( image )
sitk.Show ( 127 * ( image + eroded ), "CrossErosion" )

# <demo> --- stop ---

# Dilate
filter = sitk.BinaryDilateImageFilter()
filter.SetKernelRadius ( 5 ).SetForegroundValue ( 1 )
dilated = filter.Execute ( image )
sitk.Show ( 127 * ( image + dilated ), "Dilate by 5" )

# <demo> --- stop ---

# Grayscale
head = sitk.ReadImage ( dataDir + "/cthead1.png" )
sitk.Show ( head, "Head" )
sitk.Show ( sitk.GrayscaleDilate ( head ), "GrayscaleDilate Head" )
sitk.Show ( head - sitk.GrayscaleDilate ( head ), "GrayscaleDilate Difference" )

