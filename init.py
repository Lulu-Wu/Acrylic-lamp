# 系统模块
from machine import Pin
from neopixel import NeoPixel
from globalVal import globalVal
import time

# LED信号口
pin_led = Pin(27, Pin.OUT)
np = NeoPixel(pin_led, 16)

# WIFi连接
def WiFi_connect(wifi_name, wifi_password):
    if globalVal.in_ble_comm == 0:
        import json
        import network
        old_wifi_name = ''
        # 尝试读取配置文件wifi_confi.json,这里我们以json的方式来存储WIFI配置
        
        # 若不是初次运行,则将文件中的内容读取并加载到字典变量 config
        try:
            with open('wifi_config.json','r') as f:
                config = json.loads(f.read())
                old_wifi_name = config['essid']
                if wifi_name != 'null' and (config['essid'] != wifi_name or config['password'] != wifi_password):
                    config['essid'] = wifi_name
                    config['password'] = wifi_password
        # 若初次运行,则将进入excpet,执行配置文件的创建        
        except:
            config = dict(essid = wifi_name, password = wifi_password) # 创建字典
    #         with open('wifi_config.json','w') as f:
    #             f.write(json.dumps(config)) # 将字典序列化为json字符串,存入wifi_config.json
                
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        print("两次wifi名称差异：",old_wifi_name, wifi_name)
        if ((not wlan.isconnected()) or (wifi_name != 'null' and old_wifi_name != wifi_name)):
            wlan.disconnect()
            print('connecting to network...')
            print(config)
            wlan.connect(config['essid'], config['password'])
            for i in range(30):
                print('第{}次尝试连接Wi-Fi热点'.format(i))
                if wlan.isconnected():
                    break
                time.sleep_ms(500) #一般睡个5-10秒
            
            if not wlan.isconnected():
                wlan.active(False) #关掉连接,免得死循环输出
                print('wifi connection error, please reconnect')
                globalVal.wifi_connect_status = 'false'
                globalVal.cur_wifi_connect_status = 'cur_false'
            else:
                if config['essid'] != 'null':
                    print('network config:', wlan.ifconfig())
                    try:
                        with open('wifi_config.json','w') as f:
                            f.write(json.dumps(config)) # 将字典序列化为json字符串,存入wifi_config.json
                        globalVal.wifi_connect_status = 'true'
                        globalVal.cur_wifi_connect_status = 'cur_true'
                        globalVal.wifi_connect_name = config['essid']
                        print(globalVal.wifi_connect_name)
                        sync_time()
                    except:
                        pass
        else:
            print('Wi-Fi has connected')
            globalVal.wifi_connect_status = 'true'
            globalVal.wifi_connect_name = config['essid']
            print(globalVal.wifi_connect_name)
    else:
        print("在ble通讯期间，不可中断!")
