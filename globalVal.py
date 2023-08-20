# 使用全局变量类进行多文件共享
from machine import RTC

class globalVal:
    first_rainbow = 1;
    mode = 0               #记录模式
    ble_comm_info = ''    #记录ble传输内容类型 wifi、mode、design、get_wifi_name
    in_ble_comm = 0       #记录是否在ble通讯期间
    wifi_connect_status = 'false' #false代表WiFi未连接
    wifi_connect_name = ''   #记录当前连接WiFi名称
    cur_wifi_connect_status = 'cur_false' #代表ble单次连接WiFi状态

# 定义常量类
class const:
    MIN_WIDTH_BG = 0
    MIN_HEIGHT_BG = 0
    MAX_WIDTH_BG = 4
    MAX_HEIGHT_BG = 4
    
    MAX_LED_NUM = 16