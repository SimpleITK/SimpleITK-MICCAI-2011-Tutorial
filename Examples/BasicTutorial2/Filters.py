# Welcome to the Filters demo
print 'SimpleITK Filters'

# <demo> auto

# Every demo starts by importing the SimpleITK module
import SimpleITK as sitk

# <demo> stop

# Find some data
import os
dataDir = os.environ["HOME"] + "/src/SimpleITK/Testing/Data/Input"
image = sitk.ReadImage ( dataDir + "/RA-Short.nrrd" )
sitk.Show ( image )

# <demo> --- stop ---

# Simple smoothing
smooth = sitk.SmoothingRecursiveGaussian ( image, 2.0 )
sitk.Show ( smooth )

# <demo> --- stop ---

# Tired of typing SmoothingRecursiveGaussian ?
Gaussian = sitk.SmoothingRecursiveGaussian
smooth = Gaussian ( image, 4. )
sitk.Show ( smooth )

# <demo> --- stop ---

# Show the difference between the original and smoothed
sitk.Show ( sitk.Subtract ( image, smooth ) )

# Boom! Back to slides to explain!

# <demo> --- stop ---

# Much better
print "Before: ", smooth.GetPixelIDTypeAsString()
smooth = sitk.Cast ( smooth, image.GetPixelIDValue() )
print "After: ", smooth.GetPixelIDTypeAsString()
sitk.Show ( sitk.Subtract ( image, smooth ), "DiffWithGaussian" )

# <demo> --- stop ---

# Some other example filters

# Flip
sitk.Show ( sitk.Flip ( image ), "Flipped" )

# <demo> stop

# Canny edges
sitk.Show ( sitk.CannyEdgeDetection ( image ), "Canny" )

# <demo> stop

# Sharpen
sitk.Show ( sitk.LaplacianSharpening ( image ), "Sharp" )

# <demo> stop

# Shrink
sitk.Show ( sitk.Shrink ( image, [2,2,2] ), "Shrunk" )

# <demo> stop

# Extract
size = [64, 64, 1]
start = [64, 0, 0]
sitk.Show ( sitk.Extract ( image, size, start ), "Extracted" )
# Back to presentation

# <demo> stop

# Distance map, 25 pixels to a feature between 700 and 750
distanceMap = sitk.SignedMaurerDistanceMap ( sitk.BinaryThreshold ( image, 700, 750 ) )
sitk.Show ( sitk.IntensityWindowing ( distanceMap, 0, 25, 0, 255 ), "DistanceMap" )

# <Demo> stop

# 3D image
image = sitk.ReadImage ( dataDir + "/OAS1_0001_MR1_mpr-1_anon.nrrd" )
sitk.Show ( image )

# <demo> --- stop ---
# Flip
sitk.Show ( sitk.Flip ( image ), "Flipped" )

# <demo> stop


# Canny edges
sitk.Show ( sitk.CannyEdgeDetection ( sitk.Cast ( image, sitk.sitkFloat32 ) ), "Canny" )

# <demo> stop

# Sharpen
sitk.Show ( sitk.LaplacianSharpening ( image ), "Sharp" )

# <demo> stop

# Shrink
sitk.Show ( sitk.Shrink ( image ), [2,2,2] )

# <demo> stop
