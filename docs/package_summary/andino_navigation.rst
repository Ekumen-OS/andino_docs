andino_navigation
=================

We rely on `Nav2 <https://github.com/ros-planning/navigation2>`_ stack in order to navigate Andino.

Usage
-----

Prerequisites
^^^^^^^^^^^^^

1. Run the mobility stack in a real Andino robot or a simulated one:

   *Real robot*

   .. code-block:: bash

     ros2 launch andino_bringup andino_robot.launch.py

   *Example with Gazebo Classic*

   .. code-block:: bash

     ros2 launch andino_gz_classic andino_one_robot.launch.py

2. Provide a recorded map. Refer to :doc:`andino_slam` to learn how to record a map with Andino.

Run Nav Stack
^^^^^^^^^^^^^

.. code-block:: bash

  ros2 launch andino_navigation bringup.launch.py map:=<path-to-my-map-yaml-file>

By default, `config file <https://github.com/Ekumen-OS/andino/blob/humble/andino_navigation/params/nav2_params.yaml>`_ is used. For using a custom param file use:

.. code-block:: bash

  ros2 launch andino_navigation bringup.launch.py map:=<path-to-my-map-yaml-file> params_file:=<path-to-my-param-file>
