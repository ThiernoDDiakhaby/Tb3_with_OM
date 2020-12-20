#!/usr/bin/env python
import sys
import rospy
import cv2
import numpy as np
import time
from threading import Thread
from std_msgs.msg import Int16
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from std_srvs.srv import Empty
color_infos=(0, 255, 255)

class finish():
    def __init__(self):
    
        self.fin_sub = rospy.Subscriber("/move_fin",Int16,self.callback2)

    def callback2(self,mess):  #--- Callback function
	global fin
	fin = mess.data
	if fin == 1:
		print "Fin"
		rospy.signal_shutdown("Fin")
	
class Action(Thread):
    def __init__(self):
    	Thread.__init__(self)
    	self.pub_action = rospy.Publisher("move_action",Int16,queue_size=1)
    def run(self):
    	self.publi()
    def publi(self):
	time.sleep(5)
	while(True):
    		self.pub_action.publish(action)
		time.sleep(5)
		try:
			if fin == 1:
				break
		except NameError:
			pass

class image_converter:
    
    def __init__(self):
        #--- Publisher of the edited frame
        self.image_pub1 = rospy.Publisher("image_topic2",Image,queue_size=1)
	self.image_pub2 = rospy.Publisher("image_rouge_topic2",Image,queue_size=1)

        #--- Subscriber to the camera flow
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/color2/image_raw2",Image,self.callback)

    def callback(self,data):  #--- Callback function
	global action
        #          Conversion de l'image via cv_bridge
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
	#          Changement d'espace colorimetrique de BGR a HSVx	
        hsv_frame = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
	#          Detecter la couleur rouge
        low_red = np.array([0, 70, 50])
        high_red = np.array([10, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(cv_image, cv_image, mask=red_mask)
	red_initial=red
	elementsR=cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	if len(elementsR) > 0:
	       	c=max(elementsR, key=cv2.contourArea)
	       	((x, y), rayon)=cv2.minEnclosingCircle(c)
		cv2.circle(red, (int(x), int(y)), int(rayon), color_infos, 2)
		cv2.circle(cv_image, (int(x), int(y)), 5, color_infos, 10)
		cv2.line(cv_image, (int(x), int(y)), (int(x)+150, int(y)), color_infos, 2)
		cv2.putText(cv_image, "Objectif(Rouge) !", (int(x)+10, int(y) -10), cv2.FONT_HERSHEY_DUPLEX, 0.4, color_infos, 1, cv2.LINE_AA)
		cv2.circle(red, (int(x), int(y)), 1, color_infos, 1)
		hauteur, longeur = red.shape[:2]
		cv2.circle(red, (int(longeur/2),int(hauteur/2)),5,color_infos, 5)
		cv2.line(red, (int(x), int(y)), (int(longeur/2),int(hauteur/2)), color_infos, 2)
		Var_color=(250, max(0, 255-10*int(abs(x-longeur/2)/2)), min(150, 10*int(abs(x-longeur/2)/2)))
		if((int(y)-(hauteur/2)) > 100 or (int(y)-(hauteur/2)) < -100 or (int(x)-(longeur/2)) > 50 or (int(x)-(longeur/2)) < -50):
				if (int(y)-(hauteur/2)) > 100 :
					action = 1
				if (int(y)-(hauteur/2)) < -100 :
					action = -1
				if (int(x)-(longeur/2)) > 30 :
					cv2.arrowedLine(cv_image, (int(longeur/2),int(hauteur/2)),(int(x), int(hauteur/2)),Var_color, 1, tipLength=0.4)
					action = 2
				if (int(x)-(longeur/2)) < -30 :
					cv2.arrowedLine(cv_image, (int(longeur/2),int(hauteur/2)), (int(x), int(hauteur/2)),Var_color, 1, tipLength=0.4)
					action = -2
		else:
				cv2.putText(cv_image, "OK", (int(longeur/2),int(hauteur/2)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)
			       	action = 0

	else:
		action = 5
		
	cv2.imshow("Red", red)
	cv2.imshow("Frame", cv_image)
	cv2.waitKey(1)
	#attendre une touche
	key = cv2.waitKey(30)&0xFF
	if key == ord('q'):
		sys.exit()
		cv2.destroyAllWindows()
	if key == ord('r'):
		self.reset()
		print "reset!"

        # Publier les images modifiees dans les topics
        try:
            self.image_pub1.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
	    self.image_pub2.publish(self.bridge.cv2_to_imgmsg(red_initial, "bgr8"))
	    

        except CvBridgeError as e:
            print(e)

    def reset(self):
	rospy.wait_for_service("/gazebo/reset_world")
	reset_wold = rospy.ServiceProxy("/gazebo/reset_world",Empty)
	reset_wold()

#--------------- MAIN LOOP
def main(args):
    #--- Initialize the ROS node
    rospy.init_node('image_converter', anonymous=True)
    ic = image_converter()
    Fin = finish()
    ac= Action()
    ac.start()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    #--- In the end remember to close all cv windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
        main(sys.argv)
