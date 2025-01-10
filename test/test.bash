#!/bin/bash -xv

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source install/setup.bash && source install/local_setup.bash

timeout 20 ros2 launch mypkg talk_listen.launch.py &> /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '東京都 東京 の天気は'
