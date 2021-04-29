#!/usr/bin/python3
# Josue Becerra Rico
# Intelligent Systems and Robotics

# This script publishes the rpm of the robot to the rpm topic

# Import Libraries  
import rospy
from project_3.srv import TurnCamera, TurnCameraResponse

import os
import cv2
from cv_bridge import CvBridge

def configure_request(angle):
    rospy.wait_for_service("turn_camera")
    try:
        service_proxy = rospy.ServiceProxy("turn_camera", TurnCamera)
        resp_msg = service_proxy(angle)

        image_msg = resp_msg.image
        image = CvBridge().imgmsg_to_cv2(image_msg, desired_encoding="passthrough")
        cv2.imshow("Turn Camera Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except rospy.ServiceException as e:
        print("service request failed")
        print(e)

if __name__=='__main__': # init the node
    try:
        rospy.init_node("turn_camera_client_node")
        user_input = input("\n Enter an angle in degrees to move the robot Camera: ")
        while user_input != "q":
            try:
                configure_request(float(user_input))
                user_input = input("\n Enter an angle in degrees to move the robot camera: ")
            except:
                print("Error trying to process request")
    
    except rospy.ROSInterruptException: # Interrupt in case there is an error
        pass
