import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class virag(Node):

    def __init__(self):
        super().__init__('virag')  
        self.timer = self.create_timer(0.1, self.loop)  
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)  
        self.loop_count = 0  
        self.cycle_count = 0  

    def loop(self):
        if self.cycle_count >= 7:  
            self.get_logger().info('Virág rajzolás befejeződött.')  
            self.destroy_node()  
            rclpy.shutdown()  
            return

        cmd_msg = Twist()  

        if self.loop_count < 50:
            cmd_msg.linear.x = 1.0  
            cmd_msg.angular.z = 1.0  
        elif self.loop_count < 75:
            cmd_msg.linear.x = 0.5  
            cmd_msg.angular.z = -1.0 
        elif self.loop_count < 100:
            if self.loop_count % 2 == 0:
                cmd_msg.linear.x = 0.2  
                cmd_msg.angular.z = 1.0 
            else:
                cmd_msg.linear.x = 0.0  
                cmd_msg.angular.z = 0.0

       
        else:
            self.loop_count = 0
            self.cycle_count += 1  

        self.cmd_pub.publish(cmd_msg)
        self.loop_count += 1 

def main(args=None):
    rclpy.init(args=args) 
    viragrajzolo = virag() 
    rclpy.spin(viragrajzolo)
    viragrajzolo.destroy_node() 
    rclpy.shutdown()  
if __name__ == '__main__':
    main()
