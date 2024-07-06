import json

import requests
import base64
import cv2
import os

from PyQt5.QtCore import QThread, pyqtSignal


def show_pictures(path):
    # 百度AI开放平台车辆检测识别API的URL
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"  # 指定用于车辆型号识别的API端点

    # 打开并读取图片文件，准备进行编码
    f = open(path, 'rb')  # 以二进制读模式打开指定路径的图片文件
    img = base64.b64encode(f.read()).decode('utf-8')  # 将图片内容读取后编码为Base64字符串，并解码为UTF-8格式的字符串
    f.close()  # 关闭文件

    # 构造请求参数
    params = {"image": img, "top_num": 3}  # 将Base64编码的图片和期望返回的最可能车型数量作为参数
    access_token = '24.d31aa2ec78906dce0b6336e7c50750b3.2592000.1722826114.282335-89934939'  # 百度AI服务的访问令牌
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
    # 百度AI开放平台车辆检测识别API的URL
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"  # 指定用于车辆型号识别的API端点

    # 打开并读取图片文件，准备进行编码
    f = open(file_path, 'rb')  # 以二进制读模式打开指定路径的图片文件
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

    # 获取json
    data = response.json()

    print(data)

    result_list = []
    add_no_json = []
    add_car_json = []

    # 加载原始图像
    img = cv2.imread(file_path)
    img2 = cv2.imread('D:\AI_Summer\CarProject\GUI\copy2\other.jpg')

    # 建立存放文件夹
    output_dir = '../output_images'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 定义裁剪区域扩展的宽度和高度
    padding = 20  # 您可以根据需要调整这个值
    count = 0
    for index, item in enumerate(data['vehicle_info'], start=1):
        type = item['type']
        location = item['location']
        x1_draw = location['left']  # 用于绘制的原始位置
        y1_draw = location['top']
        x2_draw = x1_draw + location['width']
        y2_draw = y1_draw + location['height']

        # 计算裁剪时的位置，添加padding
        x1_crop = max(0, x1_draw - padding)
        y1_crop = max(0, y1_draw - padding)
        x2_crop = min(img.shape[1], x2_draw + padding)
        y2_crop = min(img.shape[0], y2_draw + padding)

        # 绘制矩形和文本（在原图上）
        cv2.rectangle(img, (x1_draw, y1_draw), (x2_draw, y2_draw), (0, 0, 255), 2)
        text = item['type']
        position = (x1_draw, y1_draw - 2)  # 文本位置通常基于绘制位置
        font = cv2.FONT_HERSHEY_SIMPLEX  # 字体
        font_scale = 1
        color = (0, 0, 255)
        thickness = 2  # 线条宽度

        # 绘制车辆类型文本
        text = item['type']
        text_position = (x1_draw, y1_draw - 2)  # 文本位置，基于矩形框的左上角调整
        cv2.putText(img, text, text_position, font, font_scale, color, thickness, cv2.LINE_AA)

        # 裁剪汽车
        if type == 'car':
            # 裁剪图像（使用调整后的位置）
            cropped_img = img2[y1_crop:y2_crop, x1_crop:x2_crop]

            # 保存裁剪的汽车照片 cropped_img
            output_path = os.path.join(output_dir, f'car_{index}.jpg')
            cv2.imwrite(output_path, cropped_img)

            # 获取列表
            output_path = 'D:/AI_Summer/CarProject/GUI/' + output_path
            result_list.append([item['type']])
            print(result_list)

            new_no_json = no_recognize(output_path, result_list[count])
            add_no_json.append(new_no_json)


            new_car_json = car_recognize(output_path, add_no_json[count])
            add_car_json.append(new_car_json)

            count = count + 1

            # 标注汽车在图中的序号
            index_position = (text_position[0], text_position[1] + len(text) * 10 + 5)  # 5是额外的间距
            index_str = str(index)  # 确保 index 是字符串类型
            cv2.putText(img, index_str, index_position, font, font_scale, color, thickness, cv2.LINE_AA)

        # 保存处理后的图像
    processed_image_path = os.path.join(os.path.dirname(file_path), "processed_image.jpg")
    cv2.imwrite(processed_image_path, img)
    print(add_car_json)
    return add_car_json


def car_recognize(path, result):
    # 百度AI开放平台车辆型号识别API的URL
    add_car_json = []
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"  # 指定用于车辆型号识别的API端点

    # 打开并读取图片文件，准备进行编码
    f = open(path, 'rb')  # 以二进制读模式打开指定路径的图片文件
    img = base64.b64encode(f.read()).decode('utf-8')  # 将图片内容读取后编码为Base64字符串，并解码为UTF-8格式的字符串
    f.close()  # 关闭文件

    # 构造请求参数
    params = {"image": img, "top_num": 1}  # 将Base64编码的图片和期望返回的最可能车型数量作为参数
    access_token = '24.73db06364d96c148581ecd77214874ea.2592000.1722415241.282335-89645117'  # 百度AI服务的访问令牌
    # 将access_token添加到请求URL中，这是进行API请求的必要认证步骤
    request_url = request_url + "?access_token=" + access_token

    # 设置请求头
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'}  # 发送Base64编码的图片，保持'application/x-www-form-urlencoded'

    # 发送POST请求
    response = requests.post(request_url, data=params, headers=headers)  # 发送POST请求

    # 处理响应
    if response.status_code == 200:  # 检查响应状态码是否为200，表示请求成功
        add_car_json = data_look(response.json(), result)

    else:
        print(f"Error: {response.status_code}, {response.text}")  # 如果请求失败，打印错误状态码和错误信息
    return add_car_json


# 车牌识别，暂定
def no_recognize(path, result):
    # 百度AI开放平台车辆型号识别API的URL
    add_no_json = []
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"  # 指定用于车辆型号识别的API端点

    # 打开并读取图片文件，准备进行编码
    f = open(path, 'rb')  # 以二进制读模式打开指定路径的图片文件
    img = base64.b64encode(f.read()).decode('utf-8')  # 将图片内容读取后编码为Base64字符串，并解码为UTF-8格式的字符串
    f.close()  # 关闭文件

    # 构造请求参数
    params = {"image": img, "top_num": 1}  # 将Base64编码的图片和期望返回的最可能车型数量作为参数
    access_token = '24.c164de1e7842856402634609fa1de5e8.2592000.1722765172.282335-91024805'  # 百度AI服务的访问令牌
    # 将access_token添加到请求URL中，这是进行API请求的必要认证步骤
    request_url = request_url + "?access_token=" + access_token

    # 设置请求头
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'}  # 发送Base64编码的图片，保持'application/x-www-form-urlencoded'

    # 发送POST请求
    response = requests.post(request_url, data=params, headers=headers)  # 发送POST请求

    # 处理响应
    if response.status_code == 200:  # 检查响应状态码是否为200，表示请求成功
        if 'error_code' in response.json():
            # 如果存在，你可以进一步处理，比如打印错误代码
            add_no_json = data_no(response.json(), result,0)
        else:
            add_no_json = data_no(response.json(), result,1)
    else:
        print(f"Error: {response.status_code}, {response.text}")  # 如果请求失败，打印错误状态码和错误信息
    return add_no_json


def data_look(look_json, result_list):
    # 遍历result列表，并提取name和year
    for item in look_json['result']:  # enumerate从1开始计数
        result_list.extend([item['name'], item['year']])
    # 打印结果
    return result_list


def data_no(no_json, result_list, stu):
    if stu == 0:
        num = '未能识别'
    else:
        num = no_json['words_result']['number']
    result_list.append(num)
    return result_list
