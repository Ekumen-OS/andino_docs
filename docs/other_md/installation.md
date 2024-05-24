# Installation

## Platforms

- ROS 2: Humble Hawksbill
- OS:
  - Ubuntu 22.04 Jammy Jellyfish
  - Ubuntu Mate 22.04 (On real robot (e.g: Raspberry Pi 4B))

## Install the binaries

The packages have been also released via ROS package manager system for the 'humble' distro. You can check them [here](https://repo.ros2.org/status_page/ros_humble_default.html?q=andino).

These packages can be installed using `apt` (e.g: `sudo apt install ros-humble-andino-description`) or using `rosdep`.

## Build from Source

### Dependencies

1. Install [ROS 2](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
2. Install [colcon](https://colcon.readthedocs.io/en/released/user/installation.html)

### colcon workspace

Packages here provided are colcon packages. As such a colcon workspace is expected:

1. Create colcon workspace

```
mkdir -p ~/ws/src
```

2. Clone this repository in the `src` folder

```
cd ~/ws/src
```

```
git clone https://github.com/Ekumen-OS/andino.git
```

3. Install dependencies via `rosdep`

```
cd ~/ws
```

```
rosdep install --from-paths src --ignore-src -i -y
```

4. Build the packages

```
colcon build
```

5. Finally, source the built packages
   If using `bash`:

```
source install/setup.bash
```

`Note`: Whether your are installing the packages in your dev machine or in your robot the procedure is the same.
