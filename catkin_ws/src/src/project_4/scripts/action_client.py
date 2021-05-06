#!/usr/bin/python3
# Josue Becerra Rico
# Intelligent Systems and Robotics

# Import Libraries  
import rospy
import actionlib
from project_4.msg import Navigate2DAction, Navigate2DFeedback, Navigate2DResult, Navigate2DGoal
from geometry_msgs.msg import Point

def action_feedback_callback(feedback):
    '''Callback function, prints distance to goal'''
    print("Distance To Goal: " + str(feedback.distance_to_point))

def nav_client(user_coords):
    ''' This function sets the goal and returns the result '''
    client = actionlib.SimpleActionClient("navigate_2D_action", Navigate2DAction)

    client.wait_for_server()

    point_msg = Point(x = user_coords[0], y = user_coords[1], z = user_coords[2])

    goal = Navigate2DGoal(point_msg)
    
    client.send_goal(goal, feedback_cb = action_feedback_callback)

    client.wait_for_result()

    return client.get_result()

if __name__ == "__main__":
    try:
        # Start node
        rospy.init_node("navigate_2D_action_client_node", anonymous=True)
        # User enter coordinates
        user_x = input("Set x-coordinate: ")
        user_y = input("Set y-coordinate: ")
        user_z = input("Set z-coordinate: ")
        # Store cordenates in list
        user_coords = [float(user_x), float(user_y), float(user_z)]
        # Call function
        result = nav_client(user_coords)
        print(result)

    except rospy.ROSInterruptException:
        print("Program Interrupted")
