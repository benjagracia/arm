import threading
import time
import RPi.GPIO as GPIO

def moverMotor(threadID,pos,v):
    count = 0
    global lines
    steps = int(lines[pos])
    while(count < steps):
        if(threadID == "Thread-1"):
            """GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(5, GPIO.HIGH)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            time.sleep(v)"""
        elif(threadID == "Thread-2"):
            """ GPIO.output(18, GPIO.HIGH)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            time.sleep(v) """
        elif(threadID == "Thread-3"):
            """ GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(v) """
        elif(threadID == "Thread-4"):
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(5, GPIO.HIGH)
            time.sleep(v)
                
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            time.sleep(v)
                
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            time.sleep(v)
        elif(threadID == "Thread-5"):
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            time.sleep(v)
            
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
            time.sleep(v)
        elif(threadID == "Thread-6"):
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(v)
            
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
            time.sleep(v)
            
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.LOW)
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(v)
        count+=1
        print(str(threadID) + " ,Step # " + str(count))
        time.sleep(v)

s = open("archivo.txt", "r")
lines = s.read()
lines = lines.replace(';',' ')
lines = lines.split(' ')
posicion = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
k=0
v=.0009
threads = []
for i in range(0,int(len(lines)/6)):
    print("Set " + str(i + 1))
    threads.clear()
    for j in range(0,6):
        t = threading.Thread(target=moverMotor, args=("Thread-" + str(j + 1),j + posicion,v))
        threads.append(t)
        t.start()
    for x in threads:
        x.join()
    posicion+=6
    print("All other threads are finished")