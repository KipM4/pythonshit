import time
import os
from pynput import keyboard

num = 0
rate = float(input("interval between counting: "))
clearpreviousnumber = input("clear previous number? (y/n): ")
start = int(input("press 1 to start counting: "))

while(start == 1):
    if clearpreviousnumber == "n":
        time.sleep(rate)
        num += 1
        print(num)   
    else:
        time.sleep(rate)
        num += 1
        os.system("cls")
        print(num)