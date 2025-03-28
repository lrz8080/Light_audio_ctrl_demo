# Light_audio_ctrl_demo
1、构建Client向Service发送请求，实现更高效灵活的控制,使用加载配置文件来一次性控制整机灯光的方法，该方法以时间细分，可控制整机任一时刻的任一灯光，同时提供了一个用于演示和测试的配置文件，配置文件位于/home/youname/light_audio_ctrl_demo/tita_ws/src/light_control/config/param.yaml

```
rgb_parameters:
  - parameters_config:
    is_head_control: true
    is_tail_control: true
    is_left_leg_control: true
    is_right_leg_control: true
    
  - serial_number: 1
    duration_ms: 200
    head_light_rgb_parameters: [
    0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,
    0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,
    0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,
    0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,
    0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,
    0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,
    0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,
    0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff]
    tail_light_rgb_parameters: [
    0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,
    0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,
    0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,0x0000ffff,
    0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,
    0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,
    0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff,0xff0000ff]
    left_leg_light_rgb_parameters: [0x0000ffff, 0x0000ffff, 0x0000ffff,
     0x0000ffff, 0x0000ffff, 0x0000ffff, 0x0000ffff, 0x0000ffff, 
     0x0000ffff, 0x0000ffff]
    right_leg_light_rgb_parameters: [0x0000ffff, 0x0000ffff, 
    0x0000ffff, 0x0000ffff, 0x0000ffff, 0x0000ffff, 0x0000ffff,
     0x0000ffff, 0x0000ffff, 0x0000ffff]


```

该表需要以rgb_parameters作为列表头，列表第一个元素是parameters_config，用来描述is_head_control is_tail_control is_left_leg_control is_right_leg_control这四个参数，当表示True时用于参与控制，并且需要用False来退出手动控制。列表后续元素是serial_number表示帧序列号，用于描述当前帧的灯效参数，需要描述的参数有duration_ms head_light_rgb_parameters tail_light_rgb_parameters left_leg_light_rgb_parameters right_leg_light_rgb_parameters，表示当前帧的持续时间、前灯灯效参数、后灯灯效参数、左腿灯灯效参数和右腿灯灯效参数，灯效参数的RGB值参考上面对各个部位灯的控制注释。

```
source /tita_ws/install/setup.bash
ros2 run light_control light_control_node 
```

**注意**
- 请不要为腿部灯条发送过高频率的请求，过高频率的请求可能会影响腿部电机通信。

2、构建Client向Service发送请求，实现自定义语音播放

- 将录制好的音频文件放到/opt/tita/sound/user目录下
```
sudo chmod +x /opt/tita/sound
source /tita_ws/install/setup.bash
ros2 run playaudio playAudio_node
```