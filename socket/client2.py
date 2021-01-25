import socket

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
s.connect(('127.0.0.1', 9090))
# 打印从服务器接收到的信息（WELCOME）
print(s.recv(1024).decode())
# 服务端向服务端发送数据
s.sendall("yuanyuan".encode())
print(s.recv(1024).decode())

s.send('exit'.encode())
s.close()

# 肯定是有预支消费缓冲区的情况，导致发送不进去
