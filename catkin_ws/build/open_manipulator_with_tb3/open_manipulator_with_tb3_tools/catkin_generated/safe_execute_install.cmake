execute_process(COMMAND "/home/diakhaby/catkin_ws/build/open_manipulator_with_tb3/open_manipulator_with_tb3_tools/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/diakhaby/catkin_ws/build/open_manipulator_with_tb3/open_manipulator_with_tb3_tools/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
