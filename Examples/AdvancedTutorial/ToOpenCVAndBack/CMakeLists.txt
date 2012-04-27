add_executable ( ToOpenCVAndBack ToOpenCVAndBack.cxx )
target_link_libraries ( ToOpenCVAndBack  ${SimpleITK_LIBRARIES} ${ITK_LIBRARIES} ${OpenCV_LIBS})

add_executable ( ToOpenCVAndBackSolution ToOpenCVAndBackSolution.cxx )
target_link_libraries ( ToOpenCVAndBackSolution  ${SimpleITK_LIBRARIES} ${ITK_LIBRARIES} ${OpenCV_LIBS})
