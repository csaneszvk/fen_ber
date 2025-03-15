import launch
from launch import LaunchDescription
from launch.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Indítjuk a turtlesim node-ot
        Node(
            package='turtlesim',  # A turtlesim csomag
            executable='turtlesim_node',  # A turtlesim node
            name='turtlesim',  # A node neve
            output='screen'  # A kimenetet a képernyőre irányítjuk
        ),
        
        # Indítjuk a virag node-ot
        Node(
            package='my_package',  # A csomag neve, ahol a virag_node.py található
            executable='virag_node',  # A virag node python scriptje
            name='virag',  # A node neve
            output='screen'  # A kimenetet a képernyőre irányítjuk
        )
    ])