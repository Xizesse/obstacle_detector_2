#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Parameters
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation time'
        ),
        
        # Obstacle Extractor Node
        Node(
            package='obstacle_detector',
            executable='obstacle_extractor_node',
            name='obstacle_extractor',
            parameters=[{
                'active': True,
                'use_scan': True,
                'use_pcl': False, 
                'use_pcl2': False,
                'use_split_and_merge': True,
                'circles_from_visibles': True,
                'discard_converted_segments': True,
                'transform_coordinates': True,
                'use_world_frame': True,  # Enable world frame transformation
                'min_group_points': 10,
                'max_group_distance': 0.1,
                'distance_proportion': 0.00628,
                'max_split_distance': 0.2,
                'max_merge_separation': 0.2,
                'max_merge_spread': 0.2,
                'max_circle_radius': 5.0,
                'radius_enlargement': 0.3,
                'frame_id': 'lidar',
                'use_sim_time': LaunchConfiguration('use_sim_time')
            }],
            
            remappings=[
                ('scan', 'scan_fixed'),
                ('pcl', '/ouster/scan'),
                ('pcl2', '/ScanMergeNode/scan_merged'),
                ('odom', '/model/agente/odometry'),  # Map odometry topic
            ]
        ),
        
        # Obstacle Tracker Node
        Node(
            package='obstacle_detector',
            executable='obstacle_tracker_node',
            name='obstacle_tracker',
            parameters=[{
                'active': True,
                'loop_rate': 100.0,
                'tracking_duration': 2.0,
                'min_correspondence_cost': 0.6,
                'std_correspondence_dev': 0.15,
                'process_variance': 0.1,
                'process_rate_variance': 0.1,
                'measurement_variance': 0.1,
                'frame_id': 'map',  # Expects world frame input
                'compensate_robot_velocity': False,  # Not needed since using world coordinates
                'use_world_coordinates': True,  # NEW: Enable world coordinate tracking with agent output
                'use_sim_time': LaunchConfiguration('use_sim_time')
            }],
            remappings=[
                ('odom', '/model/agente/odometry'),  # Map odometry for transformations
                ('tracked_obstacles', 'obstacles'),
                ('tracked_obstacles_visualization', 'obstacles_visualization')
            ]
        )
    ])

