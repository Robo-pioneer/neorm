# -*- encoding: utf-8 -*-
import socket
import sys
import threading

# TCP连接的目标机器人控制命令端口信息
tcp_host = "192.168.42.2"
tcp_port = 40923

# UDP服务器配置
udp_host = "0.0.0.0"  # 监听所有可用接口
udp_port = 50000       # UDP服务器端口

def udp_server(tcp_socket):
    """
    这个函数创建一个UDP服务器，用于接收UDP数据包，并将接收到的数据转发到TCP连接。
    """
    # 创建UDP套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.bind((udp_host, udp_port))
        print(f"UDP Server listening on {udp_host}:{udp_port}")

        while True:
            data, addr = udp_socket.recvfrom(1024)  # 接收数据
            print(f"Received from UDP ({addr}): {data.decode()}")

            # 将接收到的数据转发到TCP连接
            try:
                tcp_socket.send(data)
            except socket.error as e:
                print(f"Error sending to TCP socket: {e}")
                break

def tcp_receive(tcp_socket):
    """
    这个函数用于从TCP连接接收数据。
    """
    while True:
        try:
            buf = tcp_socket.recv(1024)
            if not buf:
                break
            print(f"Received from TCP: {buf.decode('utf-8')}")
        except socket.error as e:
            print(f"Error receiving from TCP socket: {e}")
            break

def main():
    # 创建TCP套接字并连接到机器人控制端口
    try:``
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.connect((tcp_host, tcp_port))
        print(f"Connected to TCP {tcp_host}:{tcp_port}")
    except socket.error as e:
        print(f"Error connecting to TCP socket: {e}")
        sys.exit(1)

    # 启动UDP服务器和TCP接收线程
    udp_thread = threading.Thread(target=udp_server, args=(tcp_socket,))
    tcp_thread = threading.Thread(target=tcp_receive, args=(tcp_socket,))
    udp_thread.start()
    tcp_thread.start()

    udp_thread.join()  # 等待UDP服务器线程结束
    tcp_thread.join()  # 等待TCP接收线程结束

    # 关闭TCP连接
    tcp_socket.shutdown(socket.SHUT_WR)
    tcp_socket.close()

if __name__ == '__main__':
    main()
