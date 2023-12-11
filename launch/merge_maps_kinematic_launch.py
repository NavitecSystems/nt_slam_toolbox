from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='nt_slam_toolbox',
            executable='merge_maps_kinematic',
            name='nt_slam_toolbox',
            output='screen'
        )
    ])
