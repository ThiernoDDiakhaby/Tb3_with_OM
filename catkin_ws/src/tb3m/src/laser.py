#!/usr/bin/env python
import sys
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import affiche_camera

def callback(msg):
	global A
	A = str(msg.ranges[0])
def sub():
	sub=rospy.Subscriber('/scan2',LaserScan,callback)
def laserd():
	sub()
	try:
		return A
	except NameError:
		pass
if __name__ == '__main__':
	rospy.init_node('scan_values')
	rospy.spin()

