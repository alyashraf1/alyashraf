from nanpy import (ArduinoApi, SerialManager)
from time import sleep
PWM1= 3
Motor1_1= 7
Motor1_2= 4
PWM2 = 5
Motor2_1 = 8
Motor2_2 = 12
PWM3 = 6
Motor3_1 = 13
Motor3_2 = 9
PWM4 = 10
Motor4_1 = 11
Motor4_2 = 2



def command (state):
    print(state)
    if state == "Move Straight":
        
       return  a.analogWrite(PWM1, 100), a.digitalWrite(Motor1_1,a.HIGH),a.digitalWrite(Motor1_2,a.LOW), a.analogWrite(PWM2, 100), a.digitalWrite(Motor2_1,a.HIGH), a.digitalWrite(Motor2_2,a.LOW),a.analogWrite(PWM3, 100), a.digitalWrite(Motor3_1,a.HIGH), a.digitalWrite(Motor3_2,a.LOW),a.analogWrite(PWM4,100),a.digitalWrite(Motor4_1,a.HIGH), a.digitalWrite(Motor4_2,a.LOW)
    elif state == "Turn Right":
        
        return  a.analogWrite(PWM1, 100), a.digitalWrite(Motor1_1,a.LOW),a.digitalWrite(Motor1_2,a.HIGH),a.analogWrite(PWM2, 100), a.digitalWrite(Motor2_1,a.HIGH), a.digitalWrite(Motor2_2,a.LOW),a.analogWrite(PWM3, 100), a.digitalWrite(Motor3_1,a.LOW), a.digitalWrite(Motor3_2,a.HIGH),a.analogWrite(PWM4, 100),a.digitalWrite(Motor4_1,a.HIGH), a.digitalWrite(Motor4_2,a.LOW)
    
    elif state == "Turn Left":
        return  a.analogWrite(PWM1, 100), a.digitalWrite(Motor1_1,a.HIGH),a.digitalWrite(Motor1_2,a.LOW),a.analogWrite(PWM2, 100), a.digitalWrite(Motor2_1,a.LOW), a.digitalWrite(Motor2_2,a.HIGH),a.analogWrite(PWM3, 100), a.digitalWrite(Motor3_1,a.HIGH), a.digitalWrite(Motor3_2,a.LOW),a.analogWrite(PWM4,100),a.digitalWrite(Motor4_1,a.LOW), a.digitalWrite(Motor4_2,a.HIGH)
    elif state == "Turn Back":
        return  a.analogWrite(PWM1, 100), a.digitalWrite(Motor1_1,a.LOW),a.digitalWrite(Motor1_2,a.HIGH), a.analogWrite(PWM2, 100), a.digitalWrite(Motor2_1,a.LOW), a.digitalWrite(Motor2_2,a.HIGH),a.analogWrite(PWM3, 100), a.digitalWrite(Motor3_1,a.LOW), a.digitalWrite(Motor3_2,a.HIGH),a.analogWrite(PWM4,100),a.digitalWrite(Motor4_1,a.LOW), a.digitalWrite(Motor4_2,a.HIGH)
    elif state == None:
          return  a.analogWrite(PWM1, 0), a.digitalWrite(Motor1_1,a.LOW),a.digitalWrite(Motor1_2,a.LOW), a.analogWrite(PWM2, 0), a.digitalWrite(Motor2_1,a.LOW), a.digitalWrite(Motor2_2,a.LOW),a.analogWrite(PWM3, 0), a.digitalWrite(Motor3_1,a.LOW), a.digitalWrite(Motor3_2,a.HIGH),a.analogWrite(PWM4,0),a.digitalWrite(Motor4_1,a.LOW), a.digitalWrite(Motor4_2,a.HIGH)
   
    else:
        #print("No such command")
        return 0
try:
    connection= SerialManager()
    a= ArduinoApi(connection=connection)
except:
    print("Failed to connect to Arduino")

a.pinMode(PWM1, a.OUTPUT)
a.pinMode(Motor1_1, a.OUTPUT)
a.pinMode(Motor1_2, a.OUTPUT)
a.pinMode(PWM2, a.OUTPUT)
a.pinMode(Motor2_1, a.OUTPUT)
a.pinMode(Motor2_2, a.OUTPUT)
a.pinMode(PWM3, a.OUTPUT)
a.pinMode(Motor3_1, a.OUTPUT)
a.pinMode(Motor3_2, a.OUTPUT)



    

        
        
      
    
    
    
    
    
    
    
    
    
    
