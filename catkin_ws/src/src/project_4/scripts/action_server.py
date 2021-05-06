#!/usr/bin/python3
# Josue Becerra Rico
# Intelligent Systems and Robotics

# Import Libraries  
import rospy
import actionlib
from project_4.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult
from geometry_msgs.msg import Point
import math

class Navigate2DClass:
    ''' This class starts the action, sets the goal, callback and result '''
    def __init__(self):
        # Set action server
        self.action_server = actionlib.SimpleActionServer("navigate_2D_action", Navigate2DAction, self.navigate_cb)
        # Subscribe to robot point
        self.robot_point_sub = rospy.Subscriber("robot/point", Point, self.update_robot_position)
        # Declare variables to use
        self.robot_current_point = None
        self.robot_goal_point = None
        # Set tolerance for distance accuracy
        self.distance_threshold = 0.35
        self.feedback_rate = rospy.Rate(1)

    def navigate_cb(self, goal):
        ''' Callback function'''
        # Start timer
        navigate_start_time = rospy.get_time()
        # Set goal point
        self.robot_goal_point = [goal.point.x, goal.point.y, goal.point.z]

        # Check if robot from client is detected every 5 seconds
        while self.robot_current_point == None:
            print("Robot Point Not Detected")
            rospy.sleep(2)
        # Notify when robot is detected
        print("Robot Point Detected")
        # Measure distance between current point and goal point
        distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        # Wait until distance is less than the tolerated threshold
        while distance_to_goal > self.distance_threshold:
            # Publish feedback when goal is reached
            self.action_server.publish_feedback(Navigate2DFeedback(distance_to_point = distance_to_goal))
            self.feedback_rate.sleep(2)
            # Measure distance between current point and goal point
            distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)
        
        # Stop timer
        navigate_end_time = rospy.get_time()
        
        # Calculate elapsed time
        elapsed_time = navigate_end_time - navigate_start_time

        # Log elapsed time
        rospy.loginfo("Navigation Succesful, Elapsed Time: " + str(elapsed_time) + "seconds")
        
        self.action_server.set_succeeded(Navigate2DResult(elapsed_time))
    
    def update_robot_position(self, point):
        ''' This function updates the robot position '''
        self.robot_current_point = [point.x, point.y, point.z]

if __name__=="__main__":
    # Init node
    rospy.init_node("navigate_2D_action_server_node")
    # Call class
    server = Navigate2DClass()

    rospy.spin()