import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class ServiceNode(Node):
    def __init__(self):
        super(ServiceNode, self).__init__('service_node')

        # Params
        self.declare_parameter("service_name", "")
        self.service_name_parameter = self.get_parameter("service_name").get_parameter_value().string_value
        self.declare_parameter("default_string", "")
        self.default_string_parameter = self.get_parameter("default_string").get_parameter_value().string_value
        self.string_to_store = self.default_string_parameter


        # Client
        self.client = self.create_client(Trigger, "/spgc/trigger")


        # Service
        self.service = self.create_service(Trigger, self.service_name_parameter, self.service_callback)

        self.call_spgc_trigger_service()

    def call_spgc_trigger_service(self):
        if not self.client.wait_for_service(timeout_sec=1.0):
            # self.get_logger().info('Ser -> "/spgc/trigger" not available')
            return

        request = Trigger.Request()
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.string_to_store = future.result().message
        # else:
        #     self.get_logger().info('Failed to call -> "/spgc/trigger"')


    def service_callback(self, request, response):
        response.success = True
        response.message = self.string_to_store
        return response

def main():
    rclpy.init()
    node = ServiceNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
