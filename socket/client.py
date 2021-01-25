import socket

# 创建一个 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
s.connect(('127.0.0.1', 9090))
# 打印从服务器接收到的信息（WELCOME）
print(s.recv(1).decode())  # W
print(s.recv(1).decode())  # E
print(s.recv(1024).decode())  # LCOME 不会阻塞，但缓冲区已经为空，存在预支消费，预支了 1 个字节
print(s.recv(1).decode())  # 再次recv是产生阻塞，并且无法给服务端发送消b'\x00a\x00\x00\'u\x00\x00\n\x06b1425d\x12\x0511101\x1a\x0cymyylysyqllt"\x0e192.168.88.111*,/+wn24WH+fzLg2SOfWp6HB0OuyCSL9pzJs8dW69msg8='息
# 那么如何能直接返回：
# 法一：设置非阻塞
# s.setblocking(False) # 设置非阻塞，再次消费，若不能消费到会直接抛出异常
# 法二：设置超时时间，模拟非阻塞的场景，timeout后如果再次recv还获取不到数据则抛出异常
# s.settimeout(2)
# print(s.recv(1).decode())  # 再次recv是产生阻塞，会一直等待服务端发送来的数据包
#s.sendall("yuanyuan".encode())

# 服务端再次向服务端发送数据，在recv产生阻塞时，当时客户端是不能操作的，所以不能发送成功
for data in ['yy', 'ym', 'ly', 'sy']:
    # 给服务器发信息
    s.sendall(data.encode())
    print(s.recv(1024).decode())

print(str(s.recv(1024)))  # b"\x00a\x00\x00'u\x00\x00\n\x06b1"

s.send('exit'.encode())
s.close()

# 肯定是有预支消费缓冲区的情况，导致发送不进去
