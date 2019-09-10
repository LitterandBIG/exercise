import socket

tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)


tcp_s.bind(("192.168.53.210", 8009))  #绑定端口意义，根据端口查找

tcp_s.listen(128)     #监听    负责禁用

while True:
    new_tcp, client_info = tcp_s.accept()
    #收消息
    browser_info = new_tcp.recv(2048)
    print(browser_info)
    response_head = "HTTP/1.1 200 OK\r\n\r\n"
    response_body = "hello"
    new_tcp.send((response_head+response_body).encode("utf-8"))


    new_tcp.close()





