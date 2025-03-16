import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
             package='turtlesim', 
             executable='turtlesim_node', 
             name='turtlesim',  
             output='screen' 
        ),
        
        Node(
             package='fen_ber',  
             executable='cmd_gen_node', 
             name='cmd_gen_node',  
             output='screen' 
        )
    ])