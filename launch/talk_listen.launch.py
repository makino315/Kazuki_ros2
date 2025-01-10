# SPDX-FileCopyrightText: 2025 Kazuki Makino <s23c1131km@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    weather_pub = launch_ros.actions.Node(
       package='mypkg',
       executable='weather_pub',
       )
    listener=launch_ros.actions.Node(
          package='mypkg',
          executable='listener',
          output='screen'
          )

    return launch.LaunchDescription([weather_pub,listener])

