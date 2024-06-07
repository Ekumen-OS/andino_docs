Usage
=====

Robot bringup
-------------
``andino_bringup`` contains launch files that concentrate the process that brings up the robot.

After installing and sourcing the andino's packages simply run::

   ros2 launch andino_bringup andino_robot.launch.py

This launch file initializes the differential drive controller and brings up the system to interface with ROS.
By default, sensors like the camera and the lidar are initialized. This can be disabled via arguments and manage each initialization separately. See ``ros2 launch andino_bringup andino_robot.launch.py -s`` for checking out the arguments.

- include_rplidar: ``true`` as default.
- include_camera: ``true`` as default.

After the robot is launched, use ``ROS 2 CLI`` for inspecting the environment.
For example, by doing ``ros2 topic list`` the available topics can be displayed:

   /camera_info
   /cmd_vel
   /image_raw
   /odom
   /robot_description
   /scan
   /tf
   /tf_static

   *Note: Showing just some of them*

Teleoperation
-------------
Launch files for using the keyboard or a joystick for teleoperating the robot are provided.

Keyboard
~~~~~~~~

.. code-block:: bash

   ros2 launch andino_bringup teleop_keyboard.launch.py

This is similar to just executing ``ros2 run teleop_twist_keyboard teleop_twist_keyboard``.

Joystick
~~~~~~~~
.. TODO find the way to fix these references, or change it to include other thing

Using a joystick for teleoperating is notably better.
You need the joystick configured as explained `here <andino_hardware.md#Using-joystick-for-teleoperation>`_.

.. code-block:: bash

   ros2 launch andino_bringup teleop_joystick.launch.py

RViz
----
Use:

   .. code-block:: bash

      ros2 launch andino_bringup rviz.launch.py

For starting ``rviz2`` visualization with a provided configuration.

Navigation
----------
The  `andino_navigation package <https://github.com/Ekumen-OS/andino/tree/humble/andino_navigation>`_ provides a navigation stack based on the great `Nav2 <https://github.com/ros-planning/navigation2>`_ package.

.. video:: ../_static/andino_nav2.mp4
   :width: 640
   :height: 480

Follow the :doc:`andino_navigation <package_summary/andino_navigation>` instructions for bringing up the Navigation stack in the real robot or in the simulation.

Simulation
----------
The `andino_gz_classic package <https://github.com/Ekumen-OS/andino/tree/humble/andino_gz_classic>`_ provides a Gazebo simulation for the Andino robot.
