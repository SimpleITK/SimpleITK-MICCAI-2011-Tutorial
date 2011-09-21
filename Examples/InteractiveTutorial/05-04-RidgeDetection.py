# Welcome to the Interactive Tutorial
print 'SimpleITK Interactive Tutorial'

# Every demo starts by importing the SimpleITK module
import SimpleITK as sitk

# <demo> stop
import os
dataDir = os.environ["HOME"] + "/SimpleITK-MICCAI-2011-Tutorial"
image = sitk.ReadImage ( dataDir + "/iasem-mito.nrrd" )
sitk.Show ( image, "Slice" )


# <demo> stop

diffusionFilter = sitk.GradientAnisotropicDiffusionImageFilter()
diffusionFilter.SetConductanceParameter( 1.0 )
diffusionFilter.SetNumberOfIterations( 5 )
image = diffusionFilter.Execute( sitk.Cast( image, sitk.sitkFloat32 )  )

image = sitk.Cast( image, sitk.sitkUInt8 )

sitk.Show ( image, "Diffused Slice" )
# <demo> stop


def valley_detection( img, sigma ):
    """ Detect valleys on a image at a particular scale """
    simg = sitk.SmoothingRecursiveGaussian( img, sigma )
    Lx  = sitk.Derivative( simg, 0, 1 )
    Ly  = sitk.Derivative( simg, 1, 1 )
    Lxx = sitk.Derivative( simg, 0, 2 )
    Lyy = sitk.Derivative( simg, 1, 2 )
    Lxy = sitk.Derivative( Lx, 1, 1 )
    
    Luu = Lx*Ly*(Lxx-Lyy) - ( Lx*Lx-Ly*Ly)*Lxy
    Luu2Lvv2 = ( Ly*Ly-Lx*Lx)*(Lxx-Lyy)-4*Lx*Ly*Lxy

    # Luu = = 0
    z = sitk.ZeroCrossing( Luu )

    # Luu^2 - Lvv^2 >= 0
    m = sitk.BinaryThreshold( Luu2Lvv2, 0, 1000000, 1, 0 )
    
    return z*m


# <demo> stop

r = valley_detection( image, 8 )

sitk.Show( sitk.Maximum( r*255, image ), "Ridge Detection" )

# <demo> stop
