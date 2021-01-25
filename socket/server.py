import socket
import threading


def tcp_link(sock, address):
    print('Accept new connection from %s:%s...' % address)
    # 发送信息给服务器
    sock.send('WELCOME'.encode())
    while True:
        # 接受从服务器传来的信息
        data = sock.recv(1024).decode()
        if not data or data == 'exit':
            break
        # 发送信息给服务器
        sock.send(('Hello, %s!' % data).encode())
    sock.close()
    print('Connection from %s:%s closed.' % address)


# 创建一个 socket 对象，用于 listen 和 accept
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定主机和端口
s.bind(('127.0.0.1', 9090))
# listen(n) 中 n 表示的是服务器拒绝(超过限制数量的)连接之前，操作系统可以挂起的最大连接数量
s.listen(5)
print("waiting for connection...")
while True:
    # 获取访问的客户端 socket 和 addr
    # 和 java 一样，accept 和 connect 也都是阻塞中，只允许有一个client连接
    clientSc, addr = s.accept()
    # 开启一个线程去处理与该客户端的交互
    t = threading.Thread(target=tcp_link, args=(clientSc, addr))
    t.start()
    t.join()
