import random
import math
#this is big WIP

FeelingList = ["sad", "happy", "angry", "depressed"]
EnergyList = ["asleep", "exhausted", "tired", "energetic"]
hungerList = ["malnourished", "starving", "hungry", "full", "stuffed"]

class chao:
    def __init__(self, name):
        self.name = name
        self.feelings = []
        self.energy = []
        self.hunger = []

