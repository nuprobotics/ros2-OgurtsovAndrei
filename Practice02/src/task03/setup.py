from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'task03'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/task03.launch')),
        ('share/' + package_name + '/config', glob('config/task03.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='ogurcovwm@gamil.com',
    description='Task 02 Publisher',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'task03_publisher = task03.publisher:main',
        ],
    },
)
