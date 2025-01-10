import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker=launch_ros.actions.Node(
       package='mypkg',
       executable='weather_pub',
       )
    listener=launch_ros.actions.Node(
          package='mypkg',
          executable='listener',
          output='screen'
          )

    return launch.LaunchDescription([weather_pub,listener])

