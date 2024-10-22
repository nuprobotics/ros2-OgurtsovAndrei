import rclpy
from rclpy.node import Node
from ros2topic.verb.pub import publisher
from std_msgs.msg import String


class Task02Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.declare_parameter("topic_name", "")
        self.topic_name_parameter = self.get_parameter("topic_name").get_parameter_value().string_value

        self.declare_parameter("text", "Hello, ROS2!")
        self.text_parameter = self.get_parameter("text").get_parameter_value().string_value

        # self.get_logger().info(self.text_parameter)
        # self.get_logger().info(self.topic_name_parameter)

        # self.publish_message()
        self.publisher = self.create_publisher(String, self.topic_name_parameter, 1)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = self.text_parameter
        self.publisher.publish(msg)
        # self.get_logger().info(f'{self.topic_name_parameter} -> {self.text_parameter}')



def main():
    rclpy.init()
    node = Task02Publisher()
    rclpy.spin_once(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
