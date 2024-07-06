# 基于百度API+PyQt5的车辆识别

#### 介绍
基于百度API+PyQt5的车辆识别,调用了百度的车辆检测、车型识别、车牌识别API，包括GUI、后端处理、 **项目设计文档** 

#### 软件架构
百度API+PyQt5+OpenCV，编程语言python

#### 使用说明



- :star:  :star:  :star:  **data里需要存放一个命名： **vd1.mp4**  文件 && access_token我没放** 
- data里有测试图片，建议图片放在data里
- 使用流程：运行GUI中Login.py，点击进入系统，点击上传——上传文件，点击识别——识别
- GUI文件说明：Login.py登录窗口，MainWindow主窗口，FileUploda文件上传，ByeBye视频播放
- 后端文件说明：main进行各项处理，Video视频处理
- 处理视频的代码在ByeBye窗口里,因为我的电脑只能跑几帧，而同样的代码在别的电脑里能运行流程，所以保留了视频处理但不做使用。
- requirements.txt里还有许多无关的库，本次的项目的opencv,pyqt5版本很新，应该没什么问题，建议别用requirements.txt





#### 效果演示
![登录界面](https://foruda.gitee.com/images/1720233642118080334/ab87e62a_13756960.png "屏幕截图")
![主界面](https://foruda.gitee.com/images/1720233667554523713/4fedd930_13756960.png "屏幕截图")
![拖转上传](https://foruda.gitee.com/images/1720233701505318257/3f8ff8af_13756960.png "屏幕截图")
![图片画框](https://foruda.gitee.com/images/1720234347388970249/9567e7a6_13756960.png "屏幕截图")
![列表信息](https://foruda.gitee.com/images/1720234356246768004/ae352dbc_13756960.png "屏幕截图")
> 点击按钮跳转视频
![彩蛋按钮](https://foruda.gitee.com/images/1720234390884067364/ca3d5ac8_13756960.png "屏幕截图")
![视频效果](https://foruda.gitee.com/images/1720234404485628110/1931edf1_13756960.png "屏幕截图")
