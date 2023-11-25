import socket
import threading
import re
import sys
import argparse
import os
import platform
import sys
from pathlib import Path
import torch.nn.functional as F
from Armor_Yolov5ver.utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
host = "192.168.42.2"
port = 40923
address = (host, int(port))
s = socket.socket() 
tcp = threading.Lock()


def usercode(data):
    
    print("Processed data:", data)

def process_data(data):
    # 解析并验证数据格式
    match = re.match(r'game msg push \[([0-9]+, )+([0-9]+)\];', data)
    if not match:
        return None  # 数据格式不符合，返回None

    # 提取数据
    data = match.group(0).strip('game msg push [];')
    return [int(x) for x in data.split(', ')]

def handle_client(client_data):
    # 处理客户端数据
    processed_data = process_data(client_data)
    if processed_data is not None:
        usercode(processed_data)

def udp_server():
    # 创建UDP服务器
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0.0.0.0', 40924))

    print("UDP server listening on port 40924")

    while True:
        data, addr = server.recvfrom(1024)  # 接收数据
        data = data.decode('utf-8')

        # 创建新线程处理数据
        client_thread = threading.Thread(target=handle_client, args=(data,))
        
        client_thread.start()
        
def init():
    tcp.acquire()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(address)
    tcp.release()

if __name__ == '__main__':
    init()
    udp_server()