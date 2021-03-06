#!/usr/bin/python3
# Josue Becerra Rico
# Intelligent Systems and Robotics

# This server file return the "photos" taken by the robot

# Import Libraries  
import rospy
from project_3.srv import TurnCamera, TurnCameraResponse
import os
import cv2
from cv_bridge import CvBridge

class TurnCameraClass:
    def __init__(self):
        # Define possible angles
        self.available_angles = [-30,-15,0,15,30]
        self.ros_service = rospy.Service("turn_camera", TurnCamera, self.send_image)

    def read_in_image_by_file_name(self, file_name):
        # Get working directory
        dir_name = os.path.dirname(__file__)
        file_location = dir_name + "/images/" + file_name
        # Read image using CV2 function
        image = cv2.imread(file_location)
        return image

    def get_image(self, angle):
        closest_angle = min(self.available_angles, key=lambda x:abs(x-angle))
        return self.read_in_image_by_file_name(str(closest_angle)+".png")
     #   return self.read_in_image_by_file_name("0.png")

    def send_image(self, req):
        # Get image
        image = self.get_image(req.turn_degrees)
        # Format it
        image_msg = (CvBridge().cv2_to_imgmsg(image))
        # Return image
        return TurnCameraResponse(image_msg)

if __name__=='__main__': # init the node
    try:
        rospy.init_node("turn_camera_service_node")
        TurnCameraClass()
        print("Turn Camera Service is Running")
        rospy.spin()
    
    except rospy.ROSInterruptException: # Interrupt in case there is an error
        pass
