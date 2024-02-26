#!/user/bin/env python3
import rospy
from std_msgs.msg import Int32

def call_back(data):
    output_data = (((data.data)- 10) ** 0.5)
    rospy.loginfo("The Data After Decrypting is: %d",output_data)
def subscriber():
    rospy.init_node("subscriber_node", anonymous=True)
    sub = rospy.Subscriber("first_topic", Int32, call_back)
    rospy.spin()

if __name__ == '__main__':
    subscriber()    