#!/usr/bin/env python
import sys
import rospy
import numpy as np
from std_msgs.msg import Int16
import gripper
import manip
import laser
import time


	
  
		

def main(args):
    #--- Initialize the ROS node
    rospy.init_node('Mouvement', anonymous=True)
    #--- Create the object from the class we defined before
    grip=gripper.MoveGripper()
    arm=manip.MoveArm()
    grip.gripper_close()
    arm.go_to_home_pose()
    time.sleep(3)
    arm.go_to_init_pose()
    time.sleep(4)
    grip.gripper_open()
    time.sleep(2)
    arm.go_to_home_pose()

    print("Fin de depot !")
    #--- In the end remember to close all cv windows

if __name__ == '__main__':
        main(sys.argv)
