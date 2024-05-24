# Usage

## Robot bringup

`andino_bringup` contains launch files that concentrates the process that brings up the robot.

After installing and sourcing the andino's packages simply run.

```
ros2 launch andino_bringup andino_robot.launch.py
```

This launch files initializes the differential drive controller and brings ups the system to interface with ROS.
By default sensors like the camera and the lidar are initialized. This can be disabled via arguments and manage each initialization separately. See `ros2 launch andino_bringup andino_robot.launch.py -s ` for checking out the arguments.

- include_rplidar: `true` as default.
- include_camera: `true` as default.

After the robot is launched, use `ROS 2 CLI` for inspecting environment.
For example, by doing `ros2 topic list` the available topics can be displayed:

    /camera_info
    /cmd_vel
    /image_raw
    /odom
    /robot_description
    /scan
    /tf
    /tf_static

   _Note: Showing just some of them_

## Teleoperation

Launch files for using the keyboard or a joystick for teleoperating the robot are provided.

### Keyboard

```
ros2 launch andino_bringup teleop_keyboard.launch.py
```
This is similarly to just executing `ros2 run teleop_twist_keyboard teleop_twist_keyboard`.

### Joystick

Using a joystick for teleoperating is notably better.
You need the joystick configured as explained [here](andino_hardware.md#Using-joystick-for-teleoperation).
```
ros2 launch andino_bringup teleop_joystick.launch.py
```

## RViz

Use:

```
ros2 launch andino_bringup rviz.launch.py
```

For starting `rviz2` visualization with a provided configuration.

## :compass: Navigation

The [`andino_navigation`](./andino_navigation.md) package provides a navigation stack based on the great [Nav2](https://github.com/ros-planning/navigation2) package.

https://github.com/Ekumen-OS/andino/assets/53065142/29951e74-e604-4a6e-80fc-421c0c6d8fee

Follow the [`andino_navigation`'s README](./andino_navigation.md) instructions for bringing up the Navigation stack in the real robot or in the simulation.

## :computer: Simulation

The [`andino_gz_classic`](./andino_gz_classic.md) package provides a Gazebo simulation for the Andino robot.

<img src="./andino_gz_classic/docs/andino_gz_classic.png" width=400/>
