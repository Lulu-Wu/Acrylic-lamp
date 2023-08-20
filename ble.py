import ubluetooth as bt
from bleTools import BLETools
from bleConst import BLEConst
from globalVal import globalVal

__UART_UUID = bt.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
__RX_UUID = bt.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")
__TX_UUID = bt.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")

__UART_SERVICE = (
    __UART_UUID,
    (
        (__TX_UUID, bt.FLAG_NOTIFY,),
        (__RX_UUID, bt.FLAG_WRITE,),
    ),
)


class BLEUART:
    def __init__(self, ble, rx_callback=None, name="Propylene", rxbuf=100):
        self.__ble = ble
        self.__rx_cb = rx_callback
        self.__conn_handle = None

        self.__write = self.__ble.gatts_write
        self.__read = self.__ble.gatts_read
        self.__notify = self.__ble.gatts_notify

        self.__ble.active(False)
        print("activating ble...")
        self.__ble.active(True)
        print("ble activated")

        self.__ble.config(rxbuf=rxbuf)
        self.__ble.irq(self.__irq)
        self.__register_services()

        self.__adv_payload = BLETools.advertising_generic_payload(
            services=(__UART_UUID,),
            appearance=BLEConst.Appearance.GENERIC_COMPUTER,
        )
        self.__resp_payload = BLETools.advertising_resp_payload(
            name=name
        )

        self.__advertise()

    def __register_services(self):
        (
            (
                self.__tx_handle,
                self.__rx_handle,
            ),
        ) = self.__ble.gatts_register_services((__UART_SERVICE,))

    def __advertise(self, interval_us=500000):
        self.__ble.gap_advertise(None)
        self.__ble.gap_advertise(interval_us, adv_data=self.__adv_payload, resp_data=self.__resp_payload)
        print("advertising...")
    #中断请求
    def __irq(self, event, data):
        if event == BLEConst.IRQ.IRQ_CENTRAL_CONNECT:
            self.__conn_handle, addr_type, addr, = data
            print("[{}] connected, handle: {}".format(BLETools.decode_mac(addr), self.__conn_handle))

            self.__ble.gap_advertise(None)
        elif event == BLEConst.IRQ.IRQ_CENTRAL_DISCONNECT:
            self.__conn_handle, _, addr, = data
            print("[{}] disconnected, handle: {}".format(BLETools.decode_mac(addr), self.__conn_handle))

            self.__conn_handle = None
            self.__advertise()
        elif event == BLEConst.IRQ.IRQ_GATTS_WRITE:
            conn_handle, value_handle = data

            if conn_handle == self.__conn_handle and value_handle == self.__rx_handle:
                if self.__rx_cb:
                    self.__rx_cb(self.__read(self.__rx_handle))

    def send(self, data):
        """
        将数据写入本地缓存，并推送到中心设备
        """
        self.__write(self.__tx_handle, data)

        if self.__conn_handle is not None:
            self.__notify(self.__conn_handle, self.__tx_handle, data)

wifiname_length = 0
rev_data = ''
wifi_name = ''
wifi_password = ''
rev_data_time = 0
def demo():
    from machine import Pin
    import machine
    def rx_callback(data):
        global wifiname_length
        global rev_data
        global wifi_name
        global wifi_password
        global rev_data_time
        
        globalVal.in_ble_comm = 1
        globalVal.data_transfer_end = 0
        for i in range(len(data)):
#             print(i,data[i])
            if data[i] == 2:
                print("begin receive data ...")
                globalVal.in_ble_comm = 1  #表示在数据传输阶段，不能被其他主程序或中断打断
            elif data[i] == 17:
                globalVal.ble_comm_info = 'wifi'
                wifiname_length = data[i+1]
                print(globalVal.ble_comm_info,wifiname_length)
                break
            elif data[i] == 18:
                globalVal.ble_comm_info = 'mode'
            elif data[i] == 3:
                print("end receive data ...")
                globalVal.in_ble_comm = 0  #表示ble通讯结束，不在数据传输阶段
                if globalVal.ble_comm_info == 'wifi':
                    wifi_name = rev_data[0:wifiname_length]
                    wifi_password = rev_data[wifiname_length:]
                    print("Wi-Fi name:",wifi_name, "password:", wifi_password)
                    from init import WiFi_connect
                    WiFi_connect(wifi_name, wifi_password)
                elif globalVal.ble_comm_info == 'mode':
                    pass
                else:
                    pass
                rev_data = ''
            else:
                if globalVal.ble_comm_info == 'wifi':
                    rev_data = rev_data + chr(data[i])
                elif globalVal.ble_comm_info == 'mode':
                    rev_data = chr(data[i])
                    globalVal.mode = int(rev_data)
                elif globalVal.ble_comm_info == 'get_wifi_name':
                    pass
                else:
                    pass
        
        if globalVal.ble_comm_info == 'wifi':
            if globalVal.wifi_connect_status == 'true':
                uart.send(globalVal.wifi_connect_status)
                uart.send(globalVal.wifi_connect_name)
                uart.send(globalVal.cur_wifi_connect_status)
            else:
                uart.send(globalVal.wifi_connect_status)
        if globalVal.ble_comm_info == 'get_wifi_name':
            print(globalVal.wifi_connect_name)
            uart.send(globalVal.wifi_connect_name)
            
    ble = bt.BLE()
    uart = BLEUART(ble, rx_callback)


