import socket

# 创建一个基于IPv4和TCP协议的套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口
server_address = ('127.0.0.1', 8888)
server_socket.bind(server_address)

# 监听客户端连接，最大连接数为5
server_socket.listen(5)
print('服务器已启动，正在等待客户端连接...')

while True:
    # 接受客户端连接，返回客户端套接字和客户端地址
    client_socket, client_address = server_socket.accept()
    print(f'客户端 {client_address} 已连接')

    try:
        # 接收客户端发送的数据，最多接收1024字节
        data = client_socket.recv(1024)
        if data:
            print(f'从客户端 {client_address} 接收到数据：{data.decode()}')

            # 向客户端发送响应数据
            response_data = f'你发送的数据已收到，长度为 {len(data)} 字节'
            client_socket.send(response_data.encode())
    except Exception as e:
        print(f'与客户端 {client_address} 通信时出现错误：{e}')
    finally:
        # 关闭客户端套接字
        client_socket.close()