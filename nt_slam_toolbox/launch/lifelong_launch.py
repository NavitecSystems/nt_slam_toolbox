from launch import LaunchDescription
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
          parameters=[
            get_package_share_directory("nt_slam_toolbox") + '/config/mapper_params_lifelong.yaml'
          ],
          package='nt_slam_toolbox',
          executable='lifelong_slam_toolbox_node',
          name='nt_slam_toolbox',
          output='screen'
        )
    ])
