import serial

def get_data():
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = 'COM4'
    print(ser)
    ser.open()
    if (ser.is_open):
        print("串口已连接！")
        s = ser.read(3)
        s1 = s.hex()
        #print(len(s1))
        print(s1)
        s2 =int(s1[0:6],16) #第一张卡十进制
        print(s2)
    #
        s3 = ser.read(3)
        s4 = s3.hex()
        # print(len(s1))
        print(s4)
        s5 = int(s4[0:6], 16)  # 第2张卡十进制
        print(s5)

if __name__ == '__main__':
        get_data()

