# SPDX-FileCopyrightText: 2025 Kazuki Makino <s23c1131km@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

from setuptools import setup
import os
from glob import glob
package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kazuki2',
    maintainer_email='s23c1131km@s.chibakoudai.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'weather_pub=mypkg.weather_pub:main',
            'listener=mypkg.listener:main',
        ],
    },
)
