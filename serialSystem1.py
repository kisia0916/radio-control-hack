import serial

al = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
up = ["6","2","4","1"]
down = ["5","3","7"]
right = ["8"]
left = ["0"]

def analyzeLog(log):
    log = str(log)
    if len(log.split(" ")) > 2:
        try:
            rawData = log.split(" ")[1].split("=")[1]
            dataMain = ""
            dataSub = ""
            rastIndex = 0
            if len(rawData)>0:
                for i in range(2,len(rawData)):
                    if rawData[i] in al:
                        break
                    else:
                        dataMain+=str(rawData[i])
                        rastIndex = i
                dataSub = rawData[rastIndex+1:len(rawData)-1]
                if dataMain[0] in up and len(dataMain) == 1:
                    print("up")
                    # ser2.write(str(0).encode())
                elif dataMain[0] in down:
                    print("down")
                    # ser2.write(str(1).encode())
                elif dataSub == "F8":
                    print("right")
                    # ser2.write(str(2).encode())
                elif len(dataSub) == 0 and (dataMain in al) == False:
                    print("left")
                    # ser2.write(str(3).encode())
        except:
            print("unknow")
    else:
        print(log)
# シリアルポートの設定
ser2 = serial.Serial('COM3', 115200, timeout=3)
while True:
    if ser2.in_waiting > 0:
        data = ser2.readline().decode().strip()
        analyzeLog(data)
        