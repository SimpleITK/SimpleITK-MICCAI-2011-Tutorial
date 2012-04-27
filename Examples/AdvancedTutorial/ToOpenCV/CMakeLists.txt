add_executable ( ToOpenCV ToOpenCV.cxx )
target_link_libraries ( ToOpenCV  ${SimpleITK_LIBRARIES} ${ITK_LIBRARIES} ${OpenCV_LIBS})

add_executable ( ToOpenCVSolution ToOpenCVSolution.cxx )
target_link_libraries ( ToOpenCVSolution  ${SimpleITK_LIBRARIES} ${ITK_LIBRARIES} ${OpenCV_LIBS})
