#Save on CPX/CPB as code.py 
#Blinks the top right RED LED 
import board 
import digitalio 
import analogio
import time 

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

bobs_button_B = digitalio.DigitalInOut(board.BUTTON_B)
bobs_button_B.direction = digitalio.Direction.INPUT
bobs_button_B.pull = digitalio.Pull.DOWN 

'''print(dir(board))
print('')
print(dir(digitalio))
print('')
print(dir(digitalio.DigitalInOut))
print('')
print(dir(led))
print('')
#print(dir(digitalio.Direction))'''
print("hi, its a good day")
print('--------------------')
print(dir(board))
print('--------------------')
print(dir(led))
print('--------------------')
print(dir(bobs_button_B))
print('--------------------')
print(dir(digitalio.Pull))
while True:
    led.value = bobs_button_B.value
    print(bobs_button_B.value)
    time.sleep(.2)

'''def main(): 
    print("hi")
    
    while True: 
        led.value = True 
        time.sleep(0.2) 
        led.value = False 
        time.sleep(0.2)''' 

main()
        