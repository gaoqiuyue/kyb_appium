#coding=utf-8
import os
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

def release_port(port):
    cmd_find='netstat -ano|findstr %s'%port
    result=os.popen(cmd_find).read()
    print(result)
    if str(port) and 'LISTENING' in result:
        i=result.index('LISTENING')
        start=i+len('LISTENING')+7
        end=result.index('\n')
        pid=result[start:end]
        print(pid)
        cmd_kill='taskkill -f -pid %s'%pid
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print('port %s is available !' % port)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4725
    #check_port(host,port)
    release_port(port)