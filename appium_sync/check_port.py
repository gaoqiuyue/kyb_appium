#coding=utf-8
import socket
def check_port(host,port):
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        #如果端口没有被占用，说明服务未开启，所以连接失败；如果开启了服务，就可以连接成功，那么端口就被占用了；测试连接之后，要关闭
        soc.connect((host,port))
        soc.shutdown(2)

    except OSError as msg:
        print('port %s is available! ' %port)
        print(msg)
        return True
    else:
        print('port %s already be in use !' % port)
        return False
if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4723
    check_port(host,port)