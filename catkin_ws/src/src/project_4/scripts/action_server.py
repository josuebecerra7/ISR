#!/usr/bin/python3
# Josue Becerra Rico
# Intelligent Systems and Robotics

# Import Libraries  
import rospy
import actionlib
from project_4.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult
from geometry_msgs.msg import Point

class Navigate2DClass:
    ''' This class starts the action, sets the goal, callback and result '''
    def __init__(self):
        self.action_server = actionlib.SimpleActionServer("navigate_2D_action", Navigate2DAction, self.navigate_cb)

        self.robot_point_sub = rospy.Subscriber("robot/point", Point, self.update_robot_position)

        self.robot_current_point = None

    def navigate_cb(self, goal):

        self.robot_goal_point = [goal.point.x, goal.point.y, goal.point.z]

    def update_robot_position(self, point):
        self.robot_current_point = [point.x, point.y, point.z]

        while self.robot_current_point == None:
            print("Robot Point Not Detected")

if __name__=="__main__":
    rospy.init_node("navigate_2D_action_server_node")

    server = Navigate2DClass()

    rospy.spin()