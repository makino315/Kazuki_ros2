#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 5 ros2 launch mypkg talk_listen.launch.py &> /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '東京都 東京 の天気は'
