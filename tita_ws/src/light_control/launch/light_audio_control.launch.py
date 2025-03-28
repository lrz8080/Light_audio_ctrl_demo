import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

# sys.path.insert(0, os.path.join(get_package_share_directory('tita_bringup'), 'launch'))


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='light_control',
            executable='light_control_node',
            name='light_control_node',
            output='screen',
        ),
        Node(
            package='playaudio',
            executable='playAudio_node',
            name='playAudio_node',
            output='screen',
        ),


    ])