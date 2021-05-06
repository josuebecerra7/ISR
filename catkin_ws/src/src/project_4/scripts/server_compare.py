
Skip to content

    Why GitHub?
                          


                    
Team
Enterprise
Explore
                      

                    
Marketplace
Pricing
                       


                        

Sign in
Sign up
mahnoormmalik /
ROS_Robot

1

    0

Code
Issues
Pull requests
Actions
Projects
Wiki
Security

    Insights

ROS_Robot/src/my_robot_tutorial/scripts/action_server.py /
@mahnoormmalik
mahnoormmalik Added test_sim_pkg plus comments
Latest commit 2f35882 3 days ago
History
1 contributor
executable file 86 lines (63 sloc) 3.19 KB
#!/usr/bin/env python3

""" Action Server that navigates the robot to a desired goal
This node subscribes to the "robot/point" topic to fetch the current robot co-ordinates. 
If a request is received to navigate the robot to a certain point, it navigates the robot to that point.
This file uses the Navigate2D.action file for the request, result and feedback.
"""


import rospy
import math
import actionlib
from my_robot_tutorial.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult
from geometry_msgs.msg import Point

class Navigate2DClass:
    def __init__(self):
        # Server to publish the distance to goal, callback function updates goal points
        self.action_server = actionlib.SimpleActionServer("navigate_2D_action", Navigate2DAction, self.navigate_cb)

        # Subscriber to update robot current position
        self.robot_point_subscriber = rospy.Subscriber("robot/point",Point, self.update_robot_position)

        self.robot_current_point = None
        self.robot_goal_point = None
        self.distance_threshold = 0.35
        self.feedback_rate = rospy.Rate(1)

    def navigate_cb(self, goal):
        """Handler for the Navigate2DAction server
        Takes as input the goal coordinates and navigates the robot to that point
        Parameters
        ----------
        goal: Point
            Point containing the desired x, y, and z co-ordinates of the robot
        """
        navigate_start_time = rospy.get_time()
        self.robot_goal_point = [goal.point.x, goal.point.y, goal.point.z]

        # Wait for the robot points to be published by the client
        while self.robot_current_point is None:
            print("Robot Point Not Detected")
            rospy.sleep(5)

        print("Robot Point Detected")

        # Calculate the distance to goal
        distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        # While the distance to goal is greater than the threshold value, give feedback to the client
        while distance_to_goal > self.distance_threshold:
            self.action_server.publish_feedback(Navigate2DFeedback(distance_to_point = distance_to_goal))
            # Sleeps for 1 second
            self.feedback_rate.sleep()
            
            distance_to_goal = math.dist(self.robot_current_point, self.robot_goal_point)

        # Calculate the elapsed time and send the result to the action client
        navigate_end_time = rospy.get_time()
        
        elapsed_time = navigate_end_time - navigate_start_time

        rospy.loginfo("Navigation Successful, Elapsed Time: " + str(elapsed_time) + " secs")
        self.action_server.set_succeeded(Navigate2DResult(elapsed_time))

    def update_robot_position(self, point):

        self.robot_current_point = [point.x, point.y, point.z]

if __name__ == "__main__":


    server = Navigate2DClass()

    rospy.spin()