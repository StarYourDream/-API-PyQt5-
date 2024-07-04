import json
import requests
import base64
import cv2
import os


def show_pictures(path):
    # 百度AI开放平台车辆型号识别API的URL
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"  # 指定用于车辆型号识别的API端点

    # 打开并读取图片文件，准备进行编码
    f = open(path, 'rb')  # 以二进制读模式打开指定路径的图片文件
    img = base64.b64encode(f.read()).decode('utf-8')  # 将图片内容读取后编码为Base64字符串，并解码为UTF-8格式的字符串
    f.close()  # 关闭文件

    # 构造请求参数
    params = {"image": img, "top_num": 3}  # 将Base64编码的图片和期望返回的最可能车型数量作为参数
    access_token = '24.2fcfd71dd6da73a65e54de62af80c4cd.2592000.1722495145.282335-89990893'  # 百度AI服务的访问令牌
    # 将access_token添加到请求URL中，这是进行API请求的必要认证步骤
    request_url = request_url + "?access_token=" + access_token

    # 设置请求头
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'}  # 发送Base64编码的图片，保持'application/x-www-form-urlencoded'

    # 发送POST请求
    response = requests.post(request_url, data=params, headers=headers)  # 发送POST请求

    # 处理响应
    if response.status_code == 200:  # 检查响应状态码是否为200，表示请求成功
        json_data = response.json()  # 将响应内容解析为JSON格式
        formatted_json = json.dumps(json_data, indent=4,
                                    ensure_ascii=False)  # 将JSON数据格式化为易读的字符串，包括中文（通过设置ensure_ascii=False）
        print(formatted_json)  # 打印美化后的JSON数据
    else:
        print(f"Error: {response.status_code}, {response.text}")  # 如果请求失败，打印错误状态码和错误信息
    return formatted_json


def process_image(file_path):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"

    # 读取并编码图像
    with open(file_path, 'rb') as f:
        img_bytes = f.read()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    # 发送请求
    params = {"image": img_base64, "top_num": 3}
    access_token = '24.73db06364d96c148581ecd77214874ea.2592000.1722415241.282335-89645117'
    request_url = request_url + "?access_token=" + access_token
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    data = response.json()

    # 加载原始图像
    img = cv2.imread(file_path)

    # 处理车辆检测结果
    num = data['vehicle_num']['car']
    for item in data['vehicle_info']:
        location = item['location']
        x1 = location['left']
        y1 = location['top']
        x2 = x1 + location['width']
        y2 = y1 + location['height']
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        text = item['type']
        position = (x1, y1 - 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (0, 0, 255)
        thickness = 2
        cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

    # 保存处理后的图像
    processed_image_path = os.path.join(os.path.dirname(file_path), "processed_image.jpg")
    cv2.imwrite(processed_image_path, img)

    return processed_image_path
