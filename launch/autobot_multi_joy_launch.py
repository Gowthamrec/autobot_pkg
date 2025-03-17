from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Launch Joystick Control
        ExecuteProcess(
            cmd=['terminator', '-e', 'bash -c "source /opt/ros/humble/setup.bash; source ~/ros2_ws/install/setup.bash; ros2 launch autobot_pkg joystick.launch.py; exec bash"'],
            output='screen'
        ),
        # Launch Motor Serial Node
        ExecuteProcess(
            cmd=['terminator', '-e', 'bash -c "source /opt/ros/humble/setup.bash; source ~/ros2_ws/install/setup.bash; ros2 run arduino_pkg motor_serial_node.py; exec bash"'],
            output='screen'
        )

    ])
