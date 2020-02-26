import curses
import rospy
from geometry_msgs.msg import Twist

class KeyboardInput():
    def __init__(self, stdscr):

        # No delay in getch()
        stdscr.nodelay(1)
        # initiliaze
        rospy.init_node('KeyboardInput', anonymous=False)

	# tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c
        rospy.on_shutdown(self.shutdown)

        # Create a publisher which can "talk" to TurtleBot and tell it to move
        # Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using 	TurtleBot2
        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)

        #TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to 		move? 10 HZ
        r = rospy.Rate(10);

        # as long as you haven't ctrl + c keeping doing...
        while not rospy.is_shutdown():
            # get input
            k = stdscr.getch()
            # if a key is pressed, print the numeric value of the pressed key
            # This will be updated to change the vel of the robot
            if k != -1:
                stdscr.addstr(str(c) + ' ')
                stdscr.refresh()
                stdscr.move(0,0)
	    # publish the velocity
            self.cmd_vel.publish(move_cmd)
	    # wait for 0.1 seconds (10 HZ) and publish again
            r.sleep()


    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        KeyboardInput()
    except:
        rospy.loginfo("KeyboardInput node terminated.")
