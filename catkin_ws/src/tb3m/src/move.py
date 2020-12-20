#!/usr/bin/env python
import sys
import rospy
import numpy as np
from std_msgs.msg import Int16
import gripper
import manip
import laser
import time


class mouvement():

    def __init__(self):

    	self.grip=gripper.MoveGripper()
	self.arm=manip.MoveArm()
    	self.arm.go_to_home_pose()
	self.sus_action=rospy.Subscriber("/move_action", Int16, self.callback)
    	self.pub_fin = rospy.Publisher("move_fin",Int16,queue_size=1)
	self.Suivant = False
	
  
    def callback(self,mess):
	action = mess.data
	distance= str(laser.laserd())
	self.pub_fin.publish(0)
	try:
		distance = float(distance)
	except ValueError:
		distance = 1
	if self.Suivant == False:
	    	if action == 1:
	    		# on va vers le bas
			print("bas")
			if distance > 0.1:
				self.arm.move_z(-0.02)
			else:
				self.arm.move_z(-0.005)
	    	elif action == 2:
	    		# on tourne a droite
			print("droite")
			if distance > 0.1:
				self.arm.move_y(-0.02)
			else:
				self.arm.move_y(-0.005)
	    	elif action == -1:
	    		# on va vers le haut
			print("haut")
			if distance > 0.1:
				self.arm.move_z(0.02)
			else:
				self.arm.move_z(0.005)
	    	elif action == -2:
	    		# on tourne a gauche
			print("gauche")
			if distance > 0.1:
				self.arm.move_y(0.02)
			else:
				self.arm.move_y(0.005)
			
	    	elif action == 0:
	    		#Centre
				print("centre")
				self.grip.gripper_open()
				#########################metre la bonne distance !
				if distance < 0.06:
					print("on ferme")
					#On ferme la pince				
					self.grip.gripper_close()
					if (self.grip.gripper_status == -1 ):
						self.Suivant = True
				else:
					print("on avance")
					self.grip.gripper_open()
					#On fait avancer le bras
					self.arm.move_x(0.01)
		elif action == 5:
			print distance
			if ((distance > 0.07) and (distance < 0.1)):
				print("on avance avec distance")
				self.grip.gripper_open()
				self.arm.move_x(0.01)
			elif distance < 0.7:
					print "on ferme avec distance"
					self.grip.gripper_close()
					time.sleep(2)
					self.grip.gripper_close()
					self.Suivant = True
					self.arm.go_to_home_pose()
			else:
				print "stop"
	else:
		print "on est la"
		self.grip.gripper_close()
		self.arm.go_to_home_pose()
		self.grip.gripper_close()
		for i in range(0,100):
			self.pub_fin.publish(1)
		rospy.signal_shutdown("Fin")
		

def main(args):
    #--- Initialize the ROS node
    rospy.init_node('Mouvement', anonymous=True)
    #--- Create the object from the class we defined before
    mo = mouvement()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    print("Fin de move !")
    #--- In the end remember to close all cv windows

if __name__ == '__main__':
        main(sys.argv)
