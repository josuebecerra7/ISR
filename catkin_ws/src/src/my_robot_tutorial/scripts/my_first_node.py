import rospy

if __name__=='__main__':
    rospy.init_node('my_first_python_node')
    rospy.loginfo('This node has started running')
    r= rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo("Hello world")
        r.sleep()
