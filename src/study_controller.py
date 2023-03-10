import rospy
import random
from database import dbController
from std_msgs.msg import Int8MultiArray, Int16
import time


class study_controller:
    def __init__(self):
        self.db = dbController()
        self.num_of_grasps = 40

        self.uid = 0
        self.grasp1 = 0
        self.grasp2 = 0

        rospy.init_node('web_ros')
        rospy.Subscriber('user', Int16, self.next_user)

        self.pub_grasp = rospy.Publisher('next_grasp', Int8MultiArray)
        self.view = rospy.Publisher('next_grasp', Int8MultiArray)

        time.sleep(0.1)  # add short delay

        self.next_grasp

        rospy.spin()

    def next_user(self, data):  # Iterate UID to represent a new paticipant
        self.uid = data.data
        self.next_grasp()

    def next_grasp(self):
        self.grasp1 = random.randint(0, self.num_of_grasps)
        self.grasp2 = random.randint(0, self.num_of_grasps)

        if self.grasp2 == self.grasp1:  # Verify random numbers are not the same, if they are resample
            self.next_grasp()
        else:
            pass

    def add_entry(self, pref):  # add entry db table
        self.db.addEntry(self.uid, self.grasp1, self.grasp2, pref)
        self.next_grasp()

    def disp_grasp(self, idx):
        if idx == 1:
            self.view.publish(self.grasp1)
        else if idx == 2:
            self.view.publish(self.grasp2)
