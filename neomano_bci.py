import serial
import time

def grip(interval):
    ser.write(b'1')
    time.sleep(interval)
    ser.write(b'0')
    time.sleep(interval)


def grip_test1(interval):
    ser.write(b'1')
    time.sleep(interval)
    ser.write(b'0')
    time.sleep(interval)
    time.sleep(interval)
    time.sleep(interval)
    time.sleep(interval)

def grip_test(interval):
    ser.write(b'1')
    time.sleep(interval)
    time.sleep(interval)
    time.sleep(interval)
    time.sleep(interval)
    ser.write(b'0')
    time.sleep(interval)

def release(interval):
    ser.write(b'2')
    time.sleep(interval)
    ser.write(b'0')
    time.sleep(interval)

print("Neomano BCI ver 0.1")

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM6'
ser.open()



while(1):
    nb = input('Choose a number: ')
    if nb != None:
        freq = 0.0005
        duration = 3

        if nb == '1':
            ser.write(b'1')
        elif nb == '2':
            ser.write(b'2')
        elif nb == '4':
            timeout = time.time() + duration   # 1second

            while True:
                test = 0
                if time.time() > timeout:
                    print('command done with '+str(timeout)+' seconds')
                    break
                grip(freq)
                
        elif nb == '6':
            timeout = time.time() + duration   # 1second

            while True:
                test = 0
                if time.time() > timeout:
                    print('command done with '+str(timeout)+' seconds')
                    break
                grip_test(freq)
                
        elif nb == '5':
            timeout = time.time() + duration   # 1second

            while True:
                test = 0
                if time.time() > timeout:
                    print('command done with '+str(timeout)+' seconds')
                    break
                grip_test1(freq)
                
            
        elif nb == '7':
            timeout = time.time() + duration   # 1second

            while True:
                test = 0
                if time.time() > timeout:
                    print('command done with '+str(timeout)+' seconds')
                    break
                release(freq)
            
            
        else:
            ser.write(b'0')

