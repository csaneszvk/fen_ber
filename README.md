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
ros2 launch fen_ber virag_launch.py
```

<p align="center"><img src="img/use_this_template01.png" width="60%" /></p>


Let's assume 
- your Github username is `mycoolusername`
- your ROS 2 repo shold be `cool_ros2_package`

Replace everything in the cloned repo:

- `fen_ber` >> `cool_ros2_package` (the folder was already renamed after `Use this template`)
- `csaneszvk` >> `mycoolusername`
- find all `todo` strings and fill the blanks

The easiest way is VS code:

<p align="center"><img src="img/replace01.png" width="90%" /></p>

> [!IMPORTANT]  
> Don't forget to rename the directory (folder) and the file too.

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