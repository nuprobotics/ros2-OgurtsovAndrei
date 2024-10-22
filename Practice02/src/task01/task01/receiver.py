import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ReceiverNode(Node):
    def __init__(self):
        super().__init__('receiver')
        self.subscription = self.create_subscription(
            String,
            '/spgc/sender',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'Received message: "{msg.data}"')

def main(args=None):
    print("Hello from task01.receiver")
    rclpy.init(args=args)
    receiver = ReceiverNode()
    rclpy.spin(receiver)
    receiver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
