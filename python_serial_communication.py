import serial.tools.list_ports
import flet
#
ports = serial.tools.list_ports.comports()
serialStart = serial.Serial()
#
portlist=[]
for port in ports:
    portlist.append(str(port))
    print(str(port))
secili_port = "COM3"
#
serialStart.baudrate=9600
serialStart.port=secili_port
serialStart.open()
#
try:
    while True:
        if serialStart.in_waiting:
            paket = serialStart.readline()
            print(paket.decode('utf'))
except:
    print("baglanti koptu...")


