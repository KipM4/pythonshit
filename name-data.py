name1 = input("what is your first name? ")
name2 = input("what is your last name? ")

name1lettercount = len (name1)
name2lettercount  = len (name2)
#\/im ngl i kinda forgot how i did this shit \/i
name1middle = name1[name1lettercount // 2]
name2middle = name2[name2lettercount // 2]

name1remainder = name1lettercount % 2
name2remainder = name2lettercount % 2

print(f"Your first name ({name1}) is {len (name1)} letters long")
print(f"Your last name ({name2}) is {len (name2)} letters long")

if name1lettercount > name2lettercount:
    print(f"{name1} is larger than {name2}")
    print(f"{name1} has {name1lettercount - name2lettercount} more letter(s) than {name2}")
elif name2lettercount > name1lettercount:
    print(f"{name2} is larger than {name1}")
    print(f"{name2} has {name2lettercount - name1lettercount} more letter(s) than {name1}")
else:
        print(f"{name1} and {name2} both have the same amount of letters")

if name1remainder == 0:
    print(f"{name1} doesnt have a middle letter")
else:
        print(f"{name1}s middle point is {name1[name1lettercount // 2]}")
if name2remainder == 0:
    print(f"{name2} doesnt have a middle letter")
else:
        print(f"{name2}s middle point is {name2[name2lettercount // 2]}")