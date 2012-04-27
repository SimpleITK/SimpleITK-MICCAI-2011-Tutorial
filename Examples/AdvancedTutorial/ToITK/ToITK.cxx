

#include <SimpleITK.h>

#include <cstdlib>
#include <iostream>
#include <string>

namespace sitk = itk::simple;

int main ( int argc, char **argv )
{
  if ( argc < 3 )
    {
    std::cerr << "Usage: " << argv[0] << " <input> <output>" << std::endl;
    return EXIT_FAILURE;
    }

  std::string inputFilename ( argv[1] );
  std::string outputFilename ( argv[2] );

  // Load the image via SimpleITK
  sitk::Image sitkImage = sitk::ReadImage ( inputFilename );
  if ( sitkImage.GetDimension() != 3 )
    {
    std::cerr << "Input image is required to be 3 dimensional!" << std::endl;
    return EXIT_FAILURE;
    }

  if ( sitkImage.GetPixelIDValue() != sitk::sitkFloat32 )
    {
    std::cout << "Input image is " << sitkImage.GetPixelIDTypeAsString() << " converting to float" << std::endl;
    sitkImage = sitk::Cast ( sitkImage, sitk::sitkFloat32 );
    }

  // Construct the ITK Pipeline
  // Link pipeline to SimpleITK
  // Update pipeline
  // Create output SimpleITK image
  sitk::Image sOutput = sitkImage;

  // Save image via SimpleITK
  sitk::WriteImage ( sOutput, outputFilename );
  return EXIT_SUCCESS;
}
