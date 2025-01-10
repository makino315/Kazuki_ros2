#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Kazuki Makino <s23c1131km@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

sudo apt -y install python3-pip
pip3 install requests

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source install/setup.bash && source install/local_setup.bash

timeout 20 ros2 launch mypkg talk_listen.launch.py &> /tmp/mypkg.log

cat /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '東京都 東京 の天気は'
