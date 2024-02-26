#!/user/bin/env python3
import rospy
from std_msgs.msg import Int32
import random
def publisher():
    rospy.init_node("publisher_node", anonymous= True)
    pub = rospy.Publisher("first_topic", Int32 ,queue_size = 10)
    rate = rospy.Rate(1/2)
    while not rospy.is_shutdown():
        i = random.randint(0, 10)
        a = (i ** 2) + 10    
        rospy.loginfo("Sending Encrypted Number : %d" , a)
        pub.publish(a)
        rate.sleep()

if __name__ == '__main__':
     publisher()
