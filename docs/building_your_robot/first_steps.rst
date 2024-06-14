First steps
===========

Microcontroller Configuration
-----------------------------

For uploading the microcontroller firmware please refer to :doc:`andino_firmware <../package_summary/andino_firmware>`.

Single Board Computer (SBC)
---------------------------

The SBC used in this project is a Raspberry Pi 4b so the guidelines here will refer particularly to this family of on-board computers, however extending its use to other families is possible as well.

Operative System
~~~~~~~~~~~~~~~~

Ubuntu Mate 22.04 ARM64 is the recommended operative system for this project. This OS provides good capabilities for an educational platform as well as good performance.

For installing this OS in the Raspberry:

1. Download the image from here: `ubuntu mate download <https://ubuntu-mate.org/download/arm64/>`_

2. Install OS to a microSD card using `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`_.
   - No extra configuration should be necessary.

3. Boot your raspberry using the microSD and a HDMI connection. Some initial configuration is necessary. Follow the wizard for a proper set up. It is recommended to use simple User and Password combinations for the user. For example:

    - user: pi
    - password: admin

4. Once done, run ``sudo apt update && sudo apt upgrade`` in a terminal for updating the system. Then reboot.

Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Some packages are necessary to be installed towards a correct set up of the robot's on-board computer.

ssh-server
^^^^^^^^^^

In general, you will want to access the Raspberry remotely via ``ssh`` connection while being connected in the same network.
So we need to install ``ssh-server`` and enable it if it is not enabled yet:

.. code-block:: bash

    sudo apt-get install openssh-server
    sudo systemctl enable ssh --now

After this you will be able to access this device from a remote computer by doing:

.. code-block:: bash

    ssh <user>@<ip>

For example if the user is `pi` and the ip is `192.168.0.102`

.. code-block:: bash

    ssh pi@192.168.0.102

Common utilities
^^^^^^^^^^^^^^^^

Install some common utilities that will be required later on.

.. code-block:: bash

    sudo apt update
    sudo apt install git net-tools software-properties-common build-essential -y
    sudo apt install python3-rosdep2 python3-catkin-pkg python3-catkin-pkg-modules python3-rospkg-modules python3-rospkg  -y

Install ROS
^^^^^^^^^^^

Follow these instructions to install the following dependencies from binaries:

- `ROS 2 Humble <https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html>`_
- `Colcon <https://colcon.readthedocs.io/en/released/user/installation.html>`_

To automatically source ROS installation, it is recommended to add the following line to your ``~/.bashrc`` file:

.. code-block:: bash

    source /opt/ros/humble/setup.bash

Arduino
^^^^^^^

Arduino drivers are necessary for the SBC (Raspberry) <--> Microcontroller(Arduino) serial communication.

.. code-block:: bash

    sudo apt install arduino

Configure it properly:
1. Add user to ``dialout`` and ``plugdev`` groups:

   .. code-block:: bash

       sudo usermod -a -G dialout $USER
       sudo usermod -a -G plugdev $USER

   Note you will need a reboot after this to be effective.

2. Remove ``brltty`` from the system:

   .. code-block:: bash

       sudo apt remove brltty

   In Ubuntu 22.04, there seems to be an issue with some chip drivers and the ``brltty`` daemon. To avoid this conflict, remove ``brltty`` as suggested. See `this stackoverflow post <https://stackoverflow.com/questions/70123431/why-would-ch341-uart-is-disconnected-from-ttyusb>`_ for further information.

Raspberry Camera Module V2
^^^^^^^^^^^^^^^^^^^^^^^^^^

After connecting the camera module to the Raspberry's camera port:

.. code-block:: bash

   sudo apt install libraspberrypi-bin v4l-utils
   sudo usermod -aG video $USER

Check camera status:

.. code-block:: bash

   vcgencmd get_camera

If the output of the previous command is ``supported=1 detected=1``, everything is fine. If not, your camera won't work correctly, and you need to perform some configuration first.

Modify the ``config.txt`` file for the boot:

.. code-block:: bash

   sudo nano /boot/firmware/config.txt

And add these lines:

.. code-block:: bash

   # Autoload overlays for any recognized cameras or displays that are attached
   # to the CSI/DSI ports. Please note this is for libcamera support, *not* for
   # the legacy camera stack
   start_x=1
   gpu_mem=128

Save and close the file. Then we need to enable the camera support for the Raspberry:

.. code-block:: bash

    sudo raspi-config

Go to ``Interface Options``, select ``camera`` and enable it.

Finally, you just need to reboot and the camera should be working fine.

RPLidar installation
^^^^^^^^^^^^^^^^^^^^

The installation of the A1M8 RPLidar sensor is quite straightforward, and a ROS integration package will be installed later on via `rosdep`.

For now, after connecting it to the USB port:

1. Verify USB connection: Green light in the USB converter (A1M8 side board) should be turned on.
2. Check the authority of RPLidar's serial-port:
   - Execute the following command to list available serial ports:

    .. code-block:: bash

        ls -l /dev | grep ttyUSB

   - Add extra permissions by running:

    .. code-block:: bash

        sudo chmod 666 /dev/ttyUSB<number_of_device>

USB Port name configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixed USB port names
^^^^^^^^^^^^^^^^^^^^

As having multiple USB devices connected to the USB ports of the Raspberry Pi, the automatically assigned USB port numbers could unexpectedly change after a reboot.
To avoid assigning your device to a ``tty_USBX`` number that isn't the correct onew we should assign fixed USB port name for each connected device.

The idea is to be able to generate a link between the real ``tty_USBX`` port and an invented one. For this we will need to create rules, that every time the Raspberry Pi boots are executed, and therefore we
always point to the correct port name.

In order to create fixed names for the USB devices follow the instructions:

1. Check the devices you have connected:

    .. code-block:: bash

        sudo dmesg | grep ttyUSB

    Expected output is something like the following:

    .. code-block:: bash

        [  10.016170] usb 1-1.2: ch341-uart converter now attached to ttyUSB0
        [ 309.186487] usb 1-1.1: cp210x converter now attached to ttyUSB1

    In the setup where this was tested we have:

      -> Arduino Microcontroller -> _usb 1-1.2: ch341-uart converter now attached to ``ttyUSB0``
      -> A1M8 Lidar Scanner -> _usb 1-1.1: cp210x converter now attached to ``ttyUSB1``

    *Note: If you don't know how to identify each one you can simply connect them one by one and check this output.*

2. Look for attributes for each device that we will use to anchor a particular device with a name.

    We will use the ``idProduct`` and ``idVendor`` of each device.

    - Arduino Microcontroller:

        .. code-block:: bash

            udevadm info --name=/dev/ttyUSB0 --attribute-walk

        You should look for the ``idProduct`` and ``idVendor`` under the category that matches the usb number(1-1.X):
        In this case the ``ttyUSB0`` was referenced to the ``usb 1-1.2``, so go to that section and find the ids:

        .. code-block:: bash

            ATTRS{idProduct}=="7523"
            ATTRS{idVendor}=="1a86"

    - Lidar Scanner

        .. code-block:: bash

            udevadm info --name=/dev/ttyUSB1 --attribute-walk

        In this case the ``ttyUSB0`` was referenced to the ``usb 1-1.1``, so go to that section and find the ids:

        .. code-block:: bash

            ATTRS{idProduct}=="ea60"
            ATTRS{idVendor}=="10c4"

3. Create the rules:

    Open the file:

    .. code-block:: bash

        sudo nano /etc/udev/rules.d/10-usb-serial.rules

    Add the following:

    .. code-block:: bash

        SUBSYSTEM=="tty", ATTRS{idProduct}=="7523", ATTRS{idVendor}=="1a86", SYMLINK+="ttyUSB_ARDUINO"
        SUBSYSTEM=="tty", ATTRS{idProduct}=="ea60", ATTRS{idVendor}=="10c4", SYMLINK+="ttyUSB_LIDAR"

    Note that in the `symlink` field a fixed name is indicated.

4. Re-trigger the device manager:

    .. code-block:: bash

        sudo udevadm trigger


5. Verify

    .. code-block:: bash

        ls -l /dev/ttyUSB*

    The output should be something like the following:

    .. code-block:: bash

        crw-rw---- 1 root dialout 188, 0 Sep  2 15:09 /dev/ttyUSB0
        crw-rw---- 1 root dialout 188, 1 Sep  2 15:09 /dev/ttyUSB1
        lrwxrwxrwx 1 root root         7 Sep  2 15:09 /dev/ttyUSB_ARDUINO -> ttyUSB0
        lrwxrwxrwx 1 root root         7 Sep  2 15:09 /dev/ttyUSB_LIDAR -> ttyUSB1

Done! You can always use your devices by the fixed names without using the port number.
Here, ``ttyUSB_ARDUINO`` and ``ttyUSB_LIDAR`` are fixed names for the Arduino Microcontroller and the Lidar Scanner respectively.

For more information you can take a look at this external tutorial: [Here](https://www.freva.com/assign-fixed-usb-port-names-to-your-raspberry-pi/)

Create robot workspace
~~~~~~~~~~~~~~~~~~~~~~

Let's create our workspace and build from source this repository.

.. code-block:: bash

    cd ~
    mkdir robot_ws/src -p

Clone this repository in the `src` folder

.. code-block:: bash

    cd robot_ws/src
    git clone <repository_address>

Install dependencies via rosdep:

.. code-block:: bash

    cd ~/robot_ws

When it is the first time you run ``rosdep``:

.. code-block:: bash

  rosdep update

Make sure to export the ``ROS_DISTRO`` environment variable:

.. code-block:: bash

  export ROS_DISTRO=humble

And then proceed to install the workspace dependencies:

.. code-block:: bash

  rosdep install --from-paths src -i -y -r

Note that option ``-r`` has been added. For ARM based processors, there are missing packages, e.g. those related to simulation. We would not try to run the simulation in the compute platform of andino, however for convenience it is added here.

Let's source the ROS Humble installation:

.. code-block:: bash

  source /opt/ros/humble/setup.bash

Let's build the packages (``andino_gz_classic`` and ``andino_navigation`` work only in simulation):

.. code-block:: bash

  colcon build --packages-skip andino_gz_classic andino_navigation

After building is completed:

.. code-block:: bash

  source install/setup.bash

After this, you are good to go and use the robot!
Refer to :doc:`usage <../other/usage>` section.


Extra Recommendations & Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Network
^^^^^^^

Via terminal the wifi connection can be switched by doing:

List available wifi networks:

.. code-block:: bash

  sudo nmcli dev wifi list

Connect to the desired one:

.. code-block:: bash

  sudo nmcli --ask dev wifi connect <SSID>

Copy files remotely
^^^^^^^^^^^^^^^^^^^

Using ``scp`` is a useful tool when copying files remotely over ``ssh``.

For copying a folder from host to remote unit:

.. code-block:: bash

  scp -r <path/to/folder> <remote_user>@<remote_ip>:<remote_path_to_folder>

ROS Domain ID
^^^^^^^^^^^^^

The domain ID is used by DDS to compute the UDP ports that will be used for discovery and communication.

When using a "public" network using the domain id is a good technique to avoid extra noise with other ROS 2 system in the same network.

See `ROS_DOMAIN_ID <https://docs.ros.org/en/humble/Concepts/Intermediate/About-Domain-ID.html>`_

TLDR? Export an environment variable with the same ID in **all** ROS 2 clients in the network for a correct discovery:

.. code-block:: bash

  export ROS_DOMAIN_ID=<a_number_between_0_and_101>
