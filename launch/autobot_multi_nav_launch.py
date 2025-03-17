from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Launch Gazebo with world
        ExecuteProcess(
            cmd=['terminator', '-e', 'bash -c "source /opt/ros/humble/setup.bash; source ~/ros2_ws/install/setup.bash; ros2 launch autobot_pkg autobot_gazebo.launch.py world:=./src/autobot_pkg/world/my_world_1; exec bash"'],
            output='screen'
        ),
        # Launch Online Async Process
        ExecuteProcess(
            cmd=['terminator', '-e', 'bash -c "source /opt/ros/humble/setup.bash; source ~/ros2_ws/install/setup.bash; ros2 launch autobot_pkg online_async_launch_run.launch.py; exec bash"'],
            output='screen'
        ),
        # Launch Navigation
        ExecuteProcess(
            cmd=['terminator', '-e', 'bash -c "source /opt/ros/humble/setup.bash; source ~/ros2_ws/install/setup.bash; ros2 launch autobot_pkg navigation_launch.py; exec bash"'],
            output='screen'
        ),
        # Launch RViz2
        ExecuteProcess(
            cmd=['terminator', '-e', 'bash -c "source /opt/ros/humble/setup.bash; source ~/ros2_ws/install/setup.bash; rviz2; exec bash"'],
            output='screen'
        ),
        # Launch Motor Serial Node
        ExecuteProcess(
            cmd=['terminator', '-e', 'bash -c "source /opt/ros/humble/setup.bash; source ~/ros2_ws/install/setup.bash; ros2 run arduino_pkg motor_serial_node.py; exec bash"'],
            output='screen'
        )
        
    ])
