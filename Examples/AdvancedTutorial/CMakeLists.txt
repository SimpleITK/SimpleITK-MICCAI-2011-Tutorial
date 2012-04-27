project(AdvancedTutorials)

cmake_minimum_required(VERSION 2.8)

find_package(SimpleITK REQUIRED)
include(${SimpleITK_USE_FILE})

find_package(ITK REQUIRED)
include(${ITK_USE_FILE})

find_package(OpenCV REQUIRED)
if(OpenCV_FOUND)
  include_directories(${OpenCV_INCLUDE_DIRS})
endif()

add_subdirectory ( ToITK )
add_subdirectory ( ToOpenCV )
add_subdirectory ( ToOpenCVAndBack )
