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

# First try
edges = sitk.CannyEdgeDetection( image, 100, 300, [4]*3 )

# <demo> stop

# Better
image = sitk.Cast( image, sitk.sitkFloat32 )
edges = sitk.CannyEdgeDetection( image, 100, 300, [4]*3 )

# <demo> stop

# Visualize the edges
stats = sitk.StatisticsImageFilter()
stats.Execute( image )

sitk.Show( sitk.Maximum( image, edges*stats.GetMaximum()*1.5) )
