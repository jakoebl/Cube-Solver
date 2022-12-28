import serial


arduino = serial.Serial(port="com3", baudrate=9600, timeout=.1)

arduino.write(bytes("F\r", "utf8"))

