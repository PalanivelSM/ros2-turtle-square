import rclpy # Ros client library for Python
from rclpy.node import Node 
from geometry_msgs.msg import Twist, Pose


class MoveForward(Node):

    #initialise
    def __init__(self):
            super().__init__('move_forward')
            # for rclpy we  need publisher and subscriber

            #PUblisher
            self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
            self.sub = self.create_subscription(Pose, 'tuuurtle/status_pos', 10)
            self.timer1 = self.create_timer(0.1, self.send_command)
            self.timer2 = self.create_timer(0.1, self.get_status)


    def send_command(self):
          cmd = Twist()
          cmd.linear.x = 1.0
          self.pub.publish(cmd)


    def get_status(self):
          stat = Pose()
          print(self.stat.position.x)



def main(args = None):
      rclpy.init(args = args)
      Node1 = MoveForward()
      rclpy.spin(Node1)
      Node1.destroy_node()
      rclpy.shutdown()


if __name__ == '__main__':
    main()