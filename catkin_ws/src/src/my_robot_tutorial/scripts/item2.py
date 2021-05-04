#!/usr/bin/python3
import numpy as np
import rospy
from std_msgs.msg import Float64

speed = 0

def callback(data):
    '''This function calculates speed ''' 
    global speed
    rpm = float(data.data)
    #radius = 0.2625 # radius of the wheel
    radius =rospy.get_param("/wheel_radius")
    circunference = np.pi * (radius**2) # distance in meters
    speed = circunference / (60.0/rpm) # speed in m/s
   # print("Current speed: " + str(speed) + " m/s")

def rover_speed_pub():
    # Publish speed
 #   rospy.init_node("rover_pub_speed_node") # Init node
    pub_speed = rospy.Publisher("speed", Float64, queue_size=10) # rpm topic
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub_speed.publish(speed) # rpm will be constant as defined in the requirement
        rate.sleep()

def create_subscriber():
    rospy.init_node("rover_sub_node")
    pub = rospy.Subscriber("rpm", Float64, callback)

if __name__=='__main__':
    try:
        create_subscriber()
        rover_speed_pub()
    except rospy.ROSInterruptException:
        pass