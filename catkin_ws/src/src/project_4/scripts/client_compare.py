#!/usr/bin/env python3

""" Client for the Navigate2D action server.
This node takes user input for the goal point to reach and sends a request to the navigate_2D_action server
"""

import rospy
import actionlib

from my_robot_tutorial.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult, Navigate2DGoal
from geometry_msgs.msg import Point

def feedback_callback(feedback):
    """ Callback for the action server feedback
    Prints the distance to goal
    Parameters
    ----------
    feedback: float32
        Remaining distance to goal
    """

    print("Distance To Goal: " + str(feedback.distance_to_point))

def nav_client(user_coords):
    """ Sends the goal co-ordinates to the server and returns the result
    Parameters
    ----------
    user_coords: Point
        The x, y, and z co-ordinates for the goal point
    Returns
    -------
    float32
        The elapsed time for the robot to reach the goal point
    """
    # Initialise client to publish goal coordinates to server
    client = actionlib.SimpleActionClient("navigate_2D_action", Navigate2DAction)

    client.wait_for_server()

    point_msg = Point(x = user_coords[0], y = user_coords[1], z = user_coords[2])

    goal = Navigate2DGoal(point_msg)

    client.send_goal(goal, feedback_cb = feedback_callback)

    client.wait_for_result()

    return client.get_result()

if __name__ == "__main__":
    try:
        rospy.init_node("navigate_2D_action_client_node")
        
        user_x = input("Enter the x-coordinates for the robot to move to: ")
        user_y = input("Enter the y-coordinates for the robot to move to: ")
        user_z = input("Enter the z-coordinates for the robot to move to: ")


        user_coords = [float(user_x), float(user_y), float(user_z)]

        result = nav_client(user_coords)
        print(result)

    except rospy.ROSInterruptException:
        print("Programme Interrupted")