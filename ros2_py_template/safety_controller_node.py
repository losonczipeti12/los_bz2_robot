import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SafetyControllerNode(Node):
    def __init__(self):
        super().__init__('safety_controller_node')
        self.subscription = self.create_subscription(
            Float32,
            'robot_distance',
            self.listener_callback,
            10
        )
        self.get_logger().info('Safety Controller Node elindult, figyeli az akadályokat...')

    def listener_callback(self, msg):
        distance = msg.data
        if distance < 0.5:
            self.get_logger().warn(f'VÉSZHELYZET! Akadály {distance} méterre! Robot megállítása!')
        else:
            self.get_logger().info(f'Biztonságos távolság: {distance} m')

def main(args=None):
    rclpy.init(args=args)
    safety_node = SafetyControllerNode()
    rclpy.spin(safety_node)
    safety_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
