import rclpy 
from rclpy.node import Node
import os
from tita_system_interfaces.srv import RgbControllerSrv
import asyncio 
import time 
tita_namespace ='tita'
unique_id_file ='/proc/device-tree/serial-number'
try:
    with open(unique_id_file, 'r') as file:
        unique_id = file.read().strip()
        unique_id = unique_id.replace('\x00', '')[6:]
        tita_namespace = 'tita'+unique_id
except FileNotFoundError:
        tita_namespace='tita'
except Exception as e:
        tita_namespace='tita'


class LightControl(Node):
    def __init__(self):
        super().__init__('light_control_node')
        self.client = self.create_client(RgbControllerSrv, f'/{tita_namespace}/system/light_control/rgb_control_srv')
        while not self.client.wait_for_service(timeout_sec=5.0):
                self.get_logger().info('服务不可用，正在等待服务端启动...')
        rgb_yaml_file_path='/home/robot/tita_ws/src/light_control/config/param.yaml'
        while(1):
            self.send_request(rgb_yaml_file_path)
        
        



    def send_request(self,rgb_yaml_file_path):
                # 创建服务请求
        from std_msgs.msg import String
        request = RgbControllerSrv.Request()

        request.rgb_yaml_file_path= String(data=rgb_yaml_file_path)  # 设置请求参数

        # 异步发送请求
        future = self.client.call_async(request)
        future.add_done_callback(self.callback)
    def callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info('服务调用成功!!')
            else:
                self.get_logger().info('服务调用失败!!')
        except Exception as e:
            self.get_logger().error(f'服务调用过程中发生错误: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = LightControl()
    try:
            rclpy.spin(node)
    except KeyboardInterrupt:
            pass
    finally:
        # 关闭 ROS 2 节点
            node.destroy_node()
            rclpy.shutdown()
if __name__ == '__main__':
    main()
