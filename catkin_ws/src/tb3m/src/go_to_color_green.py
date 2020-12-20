#!/usr/bin/env python
import sys
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_srvs.srv import Empty
color_infos=(0, 255, 255)
import manip
import recule
#--- Define our Class

class laser_distance:

    def __init__(self):
	self.laser_sub=rospy.Subscriber('/scan',LaserScan,self.callback)
	

    def callback(self,msg):
		global tourne
		if tourne == 1:
			if msg.ranges[0] > 0.16 and msg.ranges[1] > 0.18 and msg.ranges[2] > 0.20 and msg.ranges[3] > 0.22 and msg.ranges[23] > 0.22 and msg.ranges[22] > 0.20 and msg.ranges[21] > 0.18 and msg.ranges[20] > 0.16:
				self.avancer_gauche()
			else :
				self.tourne_gauche()
		elif tourne == -1:
			if msg.ranges[0] > 0.16 and msg.ranges[1] > 0.18 and msg.ranges[2] > 0.20 and msg.ranges[3] > 0.22 and msg.ranges[23] > 0.22 and msg.ranges[22] > 0.20 and msg.ranges[21] > 0.18 and msg.ranges[20] > 0.16:
				self.avancer_droite()
			else :
				self.tourne_droite()
		elif tourne == 0:
			if msg.ranges[0] > 0.16 and msg.ranges[1] > 0.18 and msg.ranges[2] > 0.20 and msg.ranges[3] > 0.22 and msg.ranges[23] > 0.22 and msg.ranges[22] > 0.20 and msg.ranges[21] > 0.18 and msg.ranges[20] > 0.16:
				self.avancer()
				print "Avancer !!"
			else:
				self.areter()
				print "Stop !!!"
						
		else:
			self.rapide_tourne_droite()
			print"en recheche de l'objet perdu !"


    def avancer_gauche(self):
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
	#avancer
	speed = Twist()    
	speed.linear.y = 0
        speed.linear.z = 0
        speed.angular.x = 0
        speed.angular.y = 0
        speed.angular.z = 0.05
	speed.linear.x = 0.2
	pub.publish(speed)
    def avancer_droite(self):
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
	#avancer
	speed = Twist()    
	speed.linear.y = 0
        speed.linear.z = 0
        speed.angular.x = 0
        speed.angular.y = 0
        speed.angular.z = -0.05
	speed.linear.x = 0.2
	pub.publish(speed)

    def avancer(self):
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
	#avancer
	speed = Twist()    
	speed.linear.y = 0
        speed.linear.z = 0
        speed.angular.x = 0
        speed.angular.y = 0
        speed.angular.z = 0
	speed.linear.x = 0.2
	pub.publish(speed)
    def areter(self):
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
	#areter
	speed = Twist()    
        speed.linear.x = 0
	speed.linear.y = 0
        speed.linear.z = 0
        speed.angular.x = 0
        speed.angular.y = 0
        speed.angular.z = 0
	pub.publish(speed)
    def tourne_droite(self):
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
	#areter
	speed = Twist()    
        speed.linear.x = 0
	speed.linear.y = 0
        speed.linear.z = 0
        speed.angular.x = 0
        speed.angular.y = 0
        speed.angular.z = -0.05
	pub.publish(speed)
    def rapide_tourne_droite(self):
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
	#areter
	speed = Twist()    
        speed.linear.x = 0
	speed.linear.y = 0
        speed.linear.z = 0
        speed.angular.x = 0
        speed.angular.y = 0
        speed.angular.z = -1
	pub.publish(speed)
    def tourne_gauche(self):
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)
	#areter
	speed = Twist()    
        speed.linear.x = 0
	speed.linear.y = 0
        speed.linear.z = 0
        speed.angular.x = 0
        speed.angular.y = 0
        speed.angular.z = 0.05
	pub.publish(speed)





class image_converter:
    
    def __init__(self):
        #--- Subscriber to the camera flow
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback)
	self.arm=manip.MoveArm()
    	self.arm.go_to_home_pose()
	recule.reculer()

    def callback(self,data):  #--- Callback function
	try:
		a=tourne
	except NameError:
		global tourne
		tourne=2
	try:
		Afficher = mes
	except:
		Afficher=True
        #          Conversion de l'image via cv_bridge
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
	#          Changement d'espace colorimetrique de BGR a HSVx	
        hsv_frame = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
  	low_vert = np.array([40, 40, 40])
    	high_vert = np.array([70, 255, 255])
  	vert_mask = cv2.inRange(hsv_frame, low_vert, high_vert)
    	vert = cv2.bitwise_and(cv_image, cv_image, mask=vert_mask)
	elementsR=cv2.findContours(vert_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	if len(elementsR) > 0:
	       	c=max(elementsR, key=cv2.contourArea)
	       	((x, y), rayon)=cv2.minEnclosingCircle(c)
		cv2.circle(vert, (int(x), int(y)), int(rayon), color_infos, 2)
		cv2.circle(cv_image, (int(x), int(y)), 5, color_infos, 10)
		cv2.line(cv_image, (int(x), int(y)), (int(x)+150, int(y)), color_infos, 2)
		cv2.putText(cv_image, "Objectif(vert) !", (int(x)+10, int(y) -10), cv2.FONT_HERSHEY_DUPLEX, 0.4, color_infos, 1, cv2.LINE_AA)
		cv2.circle(vert, (int(x), int(y)), 1, color_infos, 1)
		hauteur, longeur = vert.shape[:2]
		cv2.circle(vert, (int(longeur/2),int(hauteur/2)),5,color_infos, 5)
		cv2.line(vert, (int(x), int(y)), (int(longeur/2),int(hauteur/2)), color_infos, 2)
		Var_color=(0, max(255, 255-10*int(abs(x-longeur/2)/2)), min(255, 10*int(abs(x-longeur/2)/2)))		
		if (int(x)-(longeur/2)) > 5 :
			tourne = -1
			cv2.arrowedLine(cv_image, (int(longeur/2),int(hauteur/2)),(int(x), int(hauteur/2)),Var_color, 1, tipLength=0.4)
			# on tourne a droite
		elif (int(x)-(longeur/2)) < -5 :
			tourne = 1
		      	cv2.arrowedLine(cv_image, (int(longeur/2),int(hauteur/2)), (int(x), int(hauteur/2)),Var_color, 1, tipLength=0.4)
			# on tourne a gauche
		else:
			cv2.putText(cv_image, "OK", (int(longeur/2),int(hauteur/2)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)
			tourne = 0
			# C'est au millieu
			
	else:
		tourne=-2
		# on cherche l'objet !

	cv2.imshow("vert", vert)
	cv2.imshow("Frame", cv_image)
	cv2.waitKey(1)
	
	#attendre une touche
	key = cv2.waitKey(30)&0xFF
	if key == ord('q'):
		print "q"		
		sys.exit()
		cv2.destroyAllWindows()
	if key == ord('r'):
		self.reset()
		print "reset!"

    def reset(self):
	rospy.wait_for_service("/gazebo/reset_world")
	reset_wold = rospy.ServiceProxy("/gazebo/reset_world",Empty)
	reset_wold()



#--------------- MAIN LOOP
def main(args):
    print "En cour!"
    #--- Initialize the ROS node
    rospy.init_node('image_converter', anonymous=True)
    #--- Create the object from the class we defined before
    ic = image_converter()
    laser_distance()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    #--- In the end remember to close all cv windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
        main(sys.argv)
