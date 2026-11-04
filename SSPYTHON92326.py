#this is probably my least favorite program to write

#just in case my name is marcus kistler
import os
import time
import random
import math

#not sure if my codes with os.py works with linux so i heard, so.... just execute it on a windows pc
#time.sleep and os.system("cls") are just stylistic choices, they dont matter much to the actual functionality

engine_online = True
energy_level = 97.45
default_officer = "ALEX"
#these variables are just basic info about the ship

print("==============================\n\t   SS PYTHON\n==============================\n") #dont touch this
input("     press ENTER to begin ") #or this
os.system("cls")

print(f"ENGINE ONLINE = {engine_online}\nENERGY_LEVEL = {energy_level}\nDEFAULT OFFICER: {default_officer}")
time.sleep(3)

commander_name = input("COMMANDER_OVERRIDE: ")
os.system("cls")
print("NAME ACCEPTED")
time.sleep(2)
os.system("cls")
print(f"HELLO, {commander_name.upper()}")

time.sleep(2)
os.system("cls")
fuelreserve = float(input("TOTAL FUEL RESERVE (L) = "))
burnrateperlightyear = float(input("BURN RATE PER LIGHT YEAR = "))
print("\n...")
time.sleep(3)
#realistically, i dont think i would comment my code as much as i have here
totaldistance = fuelreserve / burnrateperlightyear
print(f"\nMAX TRAVEL DISTANCE = {(str(totaldistance)[0:3])} LIGHT YEAR(S)")
time.sleep(1)
os.system("cls")

missiontime = int(input("TOTAL TRAVEL TIME (S): "))
missiontimehours = missiontime // 3600
missiontimeminutes = missiontime % 3600
#/\this just seperates the travel time into minuetes and hours /\
print(f"{missiontimehours} HOURS, {missiontimeminutes} MINUTES, {missiontime} SECONDS")
time.sleep(5)
os.system("cls")

randomnumber = random.randint(100, 999)
#randomnumber is kinda vague, but it would be way to long otherwise, this is for the warp sector

print(f"EMERGENCY WARP: SECTOR {randomnumber}")
xcoord = float(input("X COORDINATE: "))
ycoord = float(input("Y COORDINATE: "))

distance = math.sqrt(math.pow(xcoord,2) + math.pow(ycoord,2)) #calculates the distance between two points, dont ask i dont really know
print("\n ...")
time.sleep(3)
print("\n[WARP COMPUTED]")
time.sleep(2)
print(f"DISTANCE = {distance} LIGHTYEARS\nENERGY NEEDED = {math.ceil(distance)}")