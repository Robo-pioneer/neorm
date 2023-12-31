import socket

def send_udp_message(message):
    server_ip = "127.0.0.1"
    server_port = 5000
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message+=';'
    try:
        # 发送消息到指定的IP地址和端口
        udp_socket.sendto(message.encode('utf-8'), (server_ip, server_port))
    finally:
        # 关闭套接字
        udp_socket.close()

if __name__ == "__main__":
    # 服务器IP和端口


    while True:
        # 获取用户输入
        user_input = input("请输入要发送的消息 (输入 'exit' 退出): ")

        # 检查用户是否想要退出
        if user_input.lower() == 'exit':
            break
        send_udp_message(user_input)
            
