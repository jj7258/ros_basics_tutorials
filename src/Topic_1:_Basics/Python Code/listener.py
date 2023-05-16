#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def chatter_callback(message):
    print("I heard ", message.data)
    #get_caller_id(): Get fully resolved name of local node
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)
    # ⬆️ This line can also be executed as well by removing the "#" and commenting the above print stmt

def listener():
    
    # Create and Initialize a ROS Node
    # ---------------------------------------
    # rospy.init_node('name_of_node',anonymous=True'to make the node unique')

    rospy.init_node('listener',anonymous=True)

    # Create a Subscriber Object
    # -------------------------------------
    # rospy.Subscriber('/topic_name',msg type of topic, callback func)
    # ---> callback function is automatically executed when a new message is heard

    rospy.Subscriber('/chatter',String, chatter_callback)

    # Starts Listening
    # -----------------------
    # rospy.spin() --> To listen for messages
    rospy.spin()

if __name__ == '__main__':
    listener()
   