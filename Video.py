import base64
import requests
from PyQt5.QtCore import QThread
import cv2
from PyQt5.QtCore import pyqtSignal


class Video(QThread):
    send = pyqtSignal(int, int, int, bytes, int)  # emit

    def __init__(self, video_id):
        super().__init__()
        # 准备工作
        # self.th_id = 0
        # # if video_id == 'data/vd1.mp4':
        self.th_id = video_id

        #self.dev = cv2.VideoCapture('../data/vd1.mp4')
        self.dev = cv2.VideoCapture('data/vd1.mp4')
        self.is_video_opened = self.dev.isOpened()
        if not self.is_video_opened:
            print("警告：无法打开视频文件")

    def run(self):

        while True:
            ret, frame = self.dev.read()
            frame = vehicle_detect(frame)
            if not ret:
                print('no')
            # car
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            print(frame.shape)
            self.send.emit(h, w, c, img_bytes, self.th_id)
            QThread.usleep(10000)


def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv2.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image": base64_image}
    access_token = '24.2fcfd71dd6da73a65e54de62af80c4cd.2592000.1722495145.282335-89990893'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        data = response.json()
        for item in data['vehicle_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            # 定义要绘制的文字
            text = item['type']
            position = (x1, y1 - 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 0, 255)  # 红色
            thickness = 2
            img = cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

    return img
