#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    # Here a new publisher  is created using the 
    # rospy.Publisher('/topic_name', date type of topic, buffer 'to create some backlog of msgs')
    pub = rospy.Publisher('/chatter',String, queue_size=10)
    # Create and Initialize a ROS Node
    # ------------------------------------------
    # rospy.init_node('name_of_node',anonymous=True'to make the node unique')
    rospy.init_node('talker',anonymous=True)

    rate = rospy.Rate(1) #Hz 
    # Rate at which data is transmitted
    # It will keep on publishing until Ctrl+C is pressed 
    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % i
        rospy.loginfo(hello_str)
        pub.publish(hello_str) # Publishing the data
        rate.sleep() # Here it'll sleep for 1 second (1/freq)
        i=i+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
