#!/usr/bin/env python
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

def all_close(goal, actual, tolerance):
  """
  Convenience method for testing if a list of values are within a tolerance of their counterparts in another list
  @param: goal       A list of floats, a	 Pose or a PoseStamped
  @param: actual     A list of floats, a Pose or a PoseStamped
  @param: tolerance  A float
  @returns: bool
  """
  all_equal = True
  if type(goal) is list:
    for index in range(len(goal)):
      if abs(actual[index] - goal[index]) > tolerance:
        return False

  elif type(goal) is geometry_msgs.msg.PoseStamped:
    return all_close(goal.pose, actual.pose, tolerance)

  elif type(goal) is geometry_msgs.msg.Pose:
    return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

  return True

class MoveGripper(object):
  """MoveGripper"""
  def __init__(self):
    moveit_commander.roscpp_initialize(sys.argv)
    #rospy.init_node('move_group_python_interface_tutorial',anonymous=True)

    robot = moveit_commander.RobotCommander()


    group_name = "gripper"
    group = moveit_commander.MoveGroupCommander(group_name)
    group_names = robot.get_group_names()

    # Misc variables
    self.robot = robot
    self.group = group
    self.group_names = group_names

  def gripper_status(self):
    group = self.group
    joint_goal = group.get_current_joint_values()
    if(joint_goal[0] > 0.01):
	return 1
    elif(joint_goal[0] < -0,3):
	return -1
    else:
	return 0

  def gripper_open(self):
    group = self.group
    joint_goal = group.get_current_joint_values()
    joint_goal[0] = 0.018
    joint_goal[1] = 0.018
    group.go(joint_goal, wait=True)
    group.stop()

    current_joints = self.group.get_current_joint_values()
    return all_close(joint_goal, current_joints, 0.01)


  def gripper_close(self):
    group = self.group
    joint_goal = group.get_current_joint_values()
    joint_goal[0] = -0.01
    joint_goal[1] = -0.01
    group.go(joint_goal, wait=True)
    group.stop()

    current_joints = self.group.get_current_joint_values()
    return all_close(joint_goal, current_joints, 0.01)


def main():
#
  #rospy.init_node('move_group_python_interface_tutorial',anonymous=True)
#
  try:
    tutorial = MoveGripper()
    print "============ Press `Enter` to execute a movement to init pose ..."
    raw_input()
    while True:
    	tutorial.affiche()



    print "============ Python tutorial demo complete!"
  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()
