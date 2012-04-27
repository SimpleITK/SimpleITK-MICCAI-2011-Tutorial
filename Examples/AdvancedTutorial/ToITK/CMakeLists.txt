add_executable ( ToITK ToITK.cxx )
target_link_libraries ( ToITK ${SimpleITK_LIBRARIES} ${ITK_LIBRARIES})

add_executable ( ToITKSolution ToITKSolution.cxx )
target_link_libraries ( ToITKSolution ${SimpleITK_LIBRARIES} ${ITK_LIBRARIES})
