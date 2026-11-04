import random
tasks = ["task1", "task2", "task3"]
random.shuffle(tasks)

person1 = input("name? ")
person2 = input("name? ")
person3 = input("name? ")

print(f"\n {person1} = {tasks[0]} \n {person2} = {tasks[1]} \n {person3} = {tasks[2]}")

