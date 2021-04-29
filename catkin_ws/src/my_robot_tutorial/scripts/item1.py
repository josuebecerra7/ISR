#!/usr/bin/python3

import time
import rospy
from std_msgs.msg import Float64

def rover_rpm_pub():
    '''Funtion that initializes the node and the publisher object to the topic rpm'''
    rospy.init_node("rover_pub_node") # Init node
    
    pub_rpm = rospy.Publisher("rpm", Float64, queue_size=10) # rpm topic

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub_rpm.publish(250) # rpm will be constant as defined in the requirement
        rate.sleep()
    

if __name__=='__main__':
    try:
        rover_rpm_pub()
    
    except rospy.ROSInterruptException:
        pass
