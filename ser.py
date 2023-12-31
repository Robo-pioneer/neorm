import socket
import threading
import re

def usercode(data):
    # 示例函数，用于处理解析后的数据
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
    print(client_data)
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

# 启动服务器
udp_server()
