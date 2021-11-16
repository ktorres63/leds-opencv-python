import serial

ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)

print("ingrese a para encender led1 y b para encender led2")
for i in range(5):
    val= input()

    if(val=='a'):
        ser.write(b'a')
    elif(val =='b'):
        ser.write(b'b')
    else:
        print("valor erroneo")
ser.close()