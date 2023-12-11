## Changes made by Navitec

- The toolbox has been renamed slam_toolbox -> nt_slam_toolbox
- The posegraph is published in the order of timestamps and the headings are assigned to the markers as well
- pause_new_measurements service is now std_srvs/srv/SetBool and takes a boolean argument to set the pause on or off
- save_map service now reports success and an optional message
- the nt_slam_toolbox adds a custom data object that contains the binary actuator state
- the pose graph is published using custom_ros2_messages/SlamPoseArray message type
