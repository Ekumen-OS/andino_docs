andino_apps
===========

This package contains integration applications with the Andino robot.

Applications
------------

Gazebo classic simulation + Nav2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A launch file for running the andino_gz_classic simulation and the Nav 2 stack is provided.
It uses the `turtlebot3_world <https://github.com/ROBOTIS-GIT/turtlebot3_simulations/tree/master>`_ world (Apache 2 license) by default.

.. code-block:: bash

    ros2 launch andino_apps andino_simulation_navigation.launch.py

To visualize and interact with the Andino robot in RViz:

- Click in 2D pose estimate button and select the initial pose of the robot
- Click in Nav2 Goal button and select the final point.
- The robot will start to move to the selected goal.

.. image:: ./media/Rviz_example_Nav2.gif

For further information and examples you can check the `Nav2 tutorials <https://docs.nav2.org/tutorials/index.html>`_.

This package has been tested with the Andino robot with `diff drive plugin` in Gazebo-classic.

By changing the world file, make sure to also change map file. Further navigation `parameters: <https://github.com/Ekumen-OS/andino/blob/humble/andino_navigation/params/nav2_params.yaml>`_ tunning is recommended.
