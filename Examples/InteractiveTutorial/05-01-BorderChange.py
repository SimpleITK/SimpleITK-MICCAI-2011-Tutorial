# Welcome to the Interactive Tutorial
print 'SimpleITK Interactive Tutorial'

# Every demo starts by importing the SimpleITK module
import SimpleITK as sitk

# <demo> stop
import os
dataDir = os.environ["HOME"] + "/Source/SimpleITK-MICCAI-2011-Tutorial"
image = sitk.ReadImage ( dataDir + "/iasem-cells.nrrd" )

# <demo> stop

print image

# <demo> stop
sitk.Show ( image, "Slice" )

# <demo> stop
image = sitk.ConstantPad( image, [0,1], [0,1], 0 )

# Threshold the value 216 results for values inside the range 1, 0
# otherwise
boundary = sitk.BinaryThreshold( image, 216, 216, 1, 0 )

# Remove any labeled pixel not connected to the boarder
boundary = sitk.BinaryGrindPeak( boundary )

sitk.Show(boundary*255 )
# <demo> stop

# remove protrusions from binary mask
boundary = sitk.BinaryMorphologicalOpening( boundary, 10  )

sitk.Show(boundary*255 )
# <demo> stop

replaceValue = 0

# Multiply, the input image by not the boarder.
# This will multiply the image by 0 or 1, where 0 is the
# boarder. Making the board 0
image *= ~boundary

# add the replace value to the pixel on the board
image += ( boundary * replaceValue )

sitk.Show( image )
