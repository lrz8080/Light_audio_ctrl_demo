import rclpy 
from rclpy.node import Node
import os
from sensor_msgs.msg import Joy
from tita_system_interfaces.srv import PlayAudioSystemPrompts
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

class PlayAudio(Node):
    def __init__(self):
        super().__init__('playAudio_node')
        self.play_client = self.create_client(PlayAudioSystemPrompts,f'/{tita_namespace}/system/audio_control/play_audio_system_prompts')
        while not self.play_client.wait_for_service(timeout_sec=5.0):
                self.get_logger().info('服务不可用，正在等待服务端启动...')
        self.joy_sub = self.create_subscription(Joy,f'/{tita_namespace}/joy',self.joy_callback,10)
        self.mark = False


    def send_request(self, audio_file_name):
        # 创建服务请求
        from std_msgs.msg import String
        request = PlayAudioSystemPrompts.Request()

        request.audio_file_name = String(data=audio_file_name)  # 设置请求参数

        # 异步发送请求
        future = self.play_client.call_async(request)
        future.add_done_callback(self.callback)

    def callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info('服务调用成功，音频播放完成！')
            else:
                self.get_logger().info('服务调用失败，音频播放未完成。')
        except Exception as e:
            self.get_logger().error(f'服务调用过程中发生错误: {e}')

    def joy_callback(self, msg):
        # self.get_logger().info('Received joy message: axes=%s' % (msg.axes))
        if msg.axes[7]==0.0:
                self.mark =True
                self.get_logger().info('%s'%(self.mark))
                if self.mark :
                        audio_file_name1='user/audio/反诈宣传歌.mp3'      
                        self.send_request(audio_file_name1)
                        time.sleep(2) #两秒
                        audio_file_name2='user/audio/7分钟网络版：公安反诈类型及防范普宣.mp3'
                        self.send_request(audio_file_name2)
                        time.sleep(2)
                        audio_file_name3='user/audio/灵魂拷问.mp3'
                        self.send_request(audio_file_name3)
                        time.sleep(2)
                        audio_file_name4='user/audio/诈骗防范音频.mp3'
                        self.send_request(audio_file_name4)
                        time.sleep(2)
                        self.mark = False
                        
                

def main(args=None):
        rclpy.init(args=args)
        node = PlayAudio()

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
