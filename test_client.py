import socket

# 创建一个基于IPv4和TCP协议的套接字对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器地址和端口
server_address = ('127.0.0.1', 8888)
client_socket.connect(server_address)

try:
    # 要发送给服务器的数据
    data_to_send = '这是客户端发送的测试数据'
    client_socket.send(data_to_send.encode())
    print(f'已向服务器发送数据：{data_to_send}')

    # 接收服务器返回的响应数据，最多接收1024字节
    response_data = client_socket.recv(1024)
    if response_data:
        print(f'从服务器接收到响应数据：{response_data.decode()}')
except Exception as e:
    print(f'与服务器通信时出现错误：{e}')
finally:
    # 关闭客户端套接字
    client_socket.close()