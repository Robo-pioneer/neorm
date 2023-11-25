# -*- encoding: utf-8 -*-
import socket
import sys
import threading

# TCP连接的目标机器人控制命令端口信息
tcp_host = "192.168.42.2"
tcp_port = 40923

# UDP服务器配置
udp_host = "0.0.0.0"  
udp_port = 50000       

def udp_server(tcp_socket):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.bind((udp_host, udp_port))
        print(f"UDP Server listening on {udp_host}:{udp_port}")

        while True:
            data, addr = udp_socket.recvfrom(1024)  # 接收数据
            print(f"Received data from {addr}: {data.decode()}")
            
            # 将接收到的数据转发到TCP连接
            try:
                tcp_socket.send(data)
            except socket.error as e:
                print(f"Error sending to TCP socket: {e}")
                break

def main():
    # 创建TCP套接字并连接到机器人控制端口
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((tcp_host, tcp_port))
        print(f"Connected to TCP {tcp_host}:{tcp_port}")
    except socket.error as e:
        print(f"Error connecting to TCP socket: {e}")
        sys.exit(1)

    # 启动UDP服务器
    udp_thread = threading.Thread(target=udp_server, args=(tcp_socket,))
    udp_thread.start()

    udp_thread.join()  # 等待UDP服务器线程结束

    # 关闭TCP连接
    tcp_socket.shutdown(socket.SHUT_WR)
    tcp_socket.close()

if __name__ == '__main__':
    main()
