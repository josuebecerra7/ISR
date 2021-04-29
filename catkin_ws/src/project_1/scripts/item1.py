#!/usr/bin/python3
# Josue Becerra Rico
# Intelligent Systems and Robotics

# This script publishes the rpm of the robot to the rpm topic

# Import Libraries  
import time
import rospy
from std_msgs.msg import Float64

def rover_rpm_pub():
    '''Funtion that initializes the node and the publisher object to the topic rpm'''
    rospy.init_node("rover_pub_node") # Init node
    
    pub_rpm = rospy.Publisher("rpm", Float64, queue_size=10) # publish rpm topic

    rate = rospy.Rate(10) # 10hz 

    while not rospy.is_shutdown():
        pub_rpm.publish(250) # rpm will be constant as defined in the requirement
        rate.sleep()
    

if __name__=='__main__': # init the node
    try:
        rover_rpm_pub()
    
    except rospy.ROSInterruptException: # Interrupt in case there is an error
        pass
