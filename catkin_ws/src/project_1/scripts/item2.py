#!/usr/bin/python3
# Josue Becerra Rico
# Intelligent Systems and Robotics

# This script reads the rpm from the rpm topic, calculates 
# the speed and publish it in speed topic

# Import Libraries  
import numpy as np
import rospy
from std_msgs.msg import Float64

# Create speed variable to be used later
speed = 0

def callback(data):
    '''This callback function calculates speed ''' 
    global speed
    rpm = float(data.data)
    #radius = 0.2625 # radius of the wheel
    ## In case the wheel_radius is set in param.yaml the next line can be used to get the radius
    radius =rospy.get_param("/wheel_radius")
    circunference = np.pi * (radius**2) # distance in meters
    speed = circunference / (60.0/rpm) # speed in m/s
   # print("Current speed: " + str(speed) + " m/s")

def rover_speed_pub():
    '''Publish speed topic'''
    #rospy.init_node("rover_pub_speed_node") # Init node
    pub_speed = rospy.Publisher("speed", Float64, queue_size=10) # speed topic
    rate = rospy.Rate(10) #10Hz
    while not rospy.is_shutdown():
        pub_speed.publish(speed) # rpm will be constant as defined in the requirement
        rate.sleep()

def create_subscriber():
    '''This function subscribes to the rpm node'''
    rospy.init_node("rover_sub_node")
    pub = rospy.Subscriber("rpm", Float64, callback)

if __name__=='__main__': # init the nodes
    try:
        create_subscriber()
        rover_speed_pub()
    except rospy.ROSInterruptException: # Interrupt in case there is an error
        pass
