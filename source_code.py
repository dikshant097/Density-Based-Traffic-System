import threading
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

led1=LED(12)
led2=LED(13)
led3=LED(14)
led4=LED(18)
led5=LED(19)
led6=LED(20)
led7=LED(24)
led8=LED(25)
led9=LED(26)


led1.on()
led2.off()
led3.off()
led4.on()
led5.off()
led6.off()
led7.on()
led8.off()
led9.off()

sleep(2)
lane=1
condition1='l'
condition2='l'
condition3='l'

def signal_timer_lane1(delay,data):
    print("lane 1 traffic condition:")
    print(data)
    print("\n")
    led1.off()
    sleep(0.25)
    led2.on()
    sleep(2)
    led2.off()
    sleep(0.25)
    led3.on() 
    sleep(delay)
    led3.off()
    sleep(0.25)
    led2.on()
    sleep(2)
    led2.off()
    sleep(0.25)
    led1.on()
    sleep(2)

def signal_timer_lane2(delay,data):
    print("lane 2 traffic condition:")
    print(data)
    print("\n")
    led4.off()
    sleep(0.25)
    led5.on()
    sleep(2)
    led5.off()
    sleep(0.25)
    led6.on() 
    sleep(delay)
    led6.off()
    sleep(0.25)
    led5.on()
    sleep(2)
    led5.off()
    sleep(0.25)
    led4.on()
    sleep(2)

def signal_timer_lane3(delay,data):
    print("lane 3 traffic condition:")
    print(data)
    print("\n")
    led7.off()
    sleep(0.25)
    led8.on()
    sleep(2)
    led8.off()
    sleep(0.25)
    led9.on() 
    sleep(delay)
    led9.off()
    sleep(0.25)
    led8.on()
    sleep(2)
    led8.off()
    sleep(0.25)
    led7.on()
    sleep(2)

def future_decision():
    loop=0
    global lane
    global condition1
    global condition2
    global condition3
    if lane==1:
	if( condition1=='l'):
			loop=2
			while loop!=0:
                                
				if ((GPIO.input(17) == GPIO.HIGH)and(GPIO.input(15) == GPIO.LOW)and(GPIO.input(16) == GPIO.LOW)):
                                    condition2='m'
                    
    
				elif((GPIO.input(15) == GPIO.LOW)and(GPIO.input(16) == GPIO.LOW)and(GPIO.input(17) == GPIO.LOW)) :
                                    condition2='h'
                    
        
				else :
                                    condition2='l'
				sleep(1.5)
				loop-=1
        elif( condition1=='m'):
                        
			loop=4
			while loop!=0:
				if ((GPIO.input(17) == GPIO.HIGH)and(GPIO.input(15) == GPIO.LOW)and(GPIO.input(16) == GPIO.LOW)):
                                        condition2='m'
                    
    
				elif((GPIO.input(17) == GPIO.LOW)and(GPIO.input(15) == GPIO.LOW)and(GPIO.input(16) == GPIO.LOW)) :
                                        condition2='h'
                    
        
				else :
                                        condition2='l'
				sleep(1.5)
				loop-=1
	else:
                        print("started")
			loop=6
			while loop!=0:
				if ((GPIO.input(17) == GPIO.HIGH)and(GPIO.input(15) == GPIO.LOW)and(GPIO.input(16) == GPIO.LOW)):
                                         condition2='m'
                    
    
				elif((GPIO.input(17) == GPIO.LOW)and(GPIO.input(15) == GPIO.LOW)and(GPIO.input(16) == GPIO.LOW)) :
                                         condition2='h'
                    
        
				else :
                                         condition2='l'
				sleep(1.5)
				loop-=1
    elif lane==2:
        if( condition2=='l'):
			loop=2
			while loop!=0:
				if ((GPIO.input(23) == GPIO.HIGH)and(GPIO.input(21) == GPIO.LOW)and(GPIO.input(22) == GPIO.LOW)):
                                        condition3='m'
                    
    
				elif((GPIO.input(23) == GPIO.LOW)and(GPIO.input(21) == GPIO.LOW)and(GPIO.input(22) == GPIO.LOW)) :
                                        condition3='h'
                    
        
				else :
                                        condition3='l'
				sleep(1.5)
				loop-=1
        elif( condition2=='m'):
			loop=4
			while loop!=0:
				if ((GPIO.input(23) == GPIO.HIGH)and(GPIO.input(21) == GPIO.LOW)and(GPIO.input(22) == GPIO.LOW)):
                                        condition3='m'
                    
    
				elif((GPIO.input(23) == GPIO.LOW)and(GPIO.input(21) == GPIO.LOW)and(GPIO.input(22) == GPIO.LOW)) :
                                        condition3='h'
                    
        
				else :
                                        condition3='l'
				sleep(1.5)
				loop-=1
	else:
			loop=6
			while loop!=0:
				if ((GPIO.input(23) == GPIO.HIGH)and(GPIO.input(21) == GPIO.LOW)and(GPIO.input(22) == GPIO.LOW)):
                                         condition3='m'
                    
    
				elif((GPIO.input(23) == GPIO.LOW)and(GPIO.input(21) == GPIO.LOW)and(GPIO.input(22) == GPIO.LOW)) :
                                         condition3='h'
                    
        
				else :
                                         condition3='l'
				sleep(1.5)
				loop-=1
                    
    else:
        if(condition3=='l'):
			loop=2
			while loop!=0:
				if ((GPIO.input(6) == GPIO.HIGH)and(GPIO.input(4) == GPIO.LOW)and(GPIO.input(5) == GPIO.LOW)):
                                        condition1='m'
                    
    
				elif((GPIO.input(4) == GPIO.LOW)and(GPIO.input(5) == GPIO.LOW)and(GPIO.input(6) == GPIO.LOW)) :
                                        condition1='h'
                    
        
                                else :
                                        condition1='l'
				sleep(1.5)
				loop-=1
        elif(condition3=='m'):
			loop=4
			while loop!=0:
				if ((GPIO.input(6) == GPIO.HIGH)and(GPIO.input(4) == GPIO.LOW)and(GPIO.input(5) == GPIO.LOW)):
                                        condition1='m'
                    
    
				elif((GPIO.input(4) == GPIO.LOW)and(GPIO.input(5) == GPIO.LOW)and(GPIO.input(6) == GPIO.LOW)) :
                                        condition1='h'
                    
        
				else :
                                        condition1='l'
				sleep(1.5)
				loop-=1
	else:
			loop=6
			while loop!=0:
				if ((GPIO.input(6) == GPIO.HIGH)and(GPIO.input(4) == GPIO.LOW)and(GPIO.input(5) == GPIO.LOW)):
                                        condition1='m'
                    
    
				elif((GPIO.input(4) == GPIO.LOW)and(GPIO.input(5) == GPIO.LOW)and(GPIO.input(6) == GPIO.LOW)) :
                                        condition1='h'
                    
        
				else :
                                        condition1='l'
				sleep(1.5)
				loop-=1
                        
if ((GPIO.input(6) == GPIO.HIGH)and(GPIO.input(4) == GPIO.LOW)and(GPIO.input(5) == GPIO.LOW)):
                    condition1='m'
		    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane1,args=(10,"medium",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
    
elif((GPIO.input(4) == GPIO.LOW)and(GPIO.input(5) == GPIO.LOW)and(GPIO.input(6) == GPIO.LOW)) :
                    condition1='h'
		    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane1,args=(15,"high",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
        
else :
                    condition1='l'
		    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane1,args=(5,"low",))
                    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
lane=2
while True :
    if lane == 2:
            lane=3
            if (condition2=='m'):
                    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane2,args=(10,"medium",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
    
            elif(condition2=='h') :
                    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane2,args=(15,"high",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
        
            else :
		    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane2,args=(5,"low",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
    elif lane==3:
            lane=1
            if (condition3=='m'):
                    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane3,args=(10,"medium",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
    
            elif(condition3=='h') :
                    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane3,args=(15,"high",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
        
            else :
                    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane3,args=(5,"low",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
    elif lane==1:
            lane=2
            if (condition1=='m'):
                    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane1,args=(10,"medium",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
    
            elif(condition1=='h') :
                    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane1,args=(15,"high",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
        
            else :
		    t1=threading.Thread(target=future_decision)
                    t2=threading.Thread(target=signal_timer_lane1,args=(5,"low",))
		    t1.start()
		    t2.start()
		    t1.join()
		    t2.join()
