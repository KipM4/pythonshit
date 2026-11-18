import random
import math
import time
#this is big WIP

FeelingList = ["sad", "happy", "angry", "depressed"]
EnergyList = ["asleep", "exhausted", "tired", "energetic"]
hungerList = ["malnourished", "starving", "hungry", "full", "stuffed"]
actionList = ["looks at the water", "says hurtful words about other people online", "is ok", "reminds you of something that you cant remember"]
class chao:
    def __init__(self, name):
        self.name = name
        self.feelings = []
        self.energy = []
        self.hunger = []
#declare chao name
chao1name = input("chao name?: ")
chao1 = chao(name=chao1name)

start_time = time.time()

#chao passively does things
while True:
    secs_passed = time.time() - start_time
    if secs_passed >= 20:
        print(f"{chao1.name} {random.choice(actionList)}")
        start_time = time.time()