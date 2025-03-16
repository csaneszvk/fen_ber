# `fen_ber` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/csaneszvk/fen_ber
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select fen_ber --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch fen_ber cmd_gen_node.py
```
Now `colcon build` your ROS 2 package and you can start wokring.
```mermaid
graph TD
    A[Start] --> B[Launch turtlesim node]
    A --> C[Launch virag node]
    
    B --> D[turtlesim_node]
    C --> E[virag_node]

    E --> F[Publish to /turtle1/cmd_vel]
    D --> G[Subscribe to /turtle1/cmd_vel]
    G --> F
```