#!/usr/bin/python3
import rospy
from std_msgs.msg import Float64

def callback(data):
    print("Speed: " + str(data.data) + " m/s")

def create_subscriber():
    rospy.init_node("speed_sub_node")
    pub = rospy.Subscriber("speed", Float64, callback)

if __name__=='__main__':
    create_subscriber()
    rospy.spin() # prevent script from closing
