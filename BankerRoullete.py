import random

names = input("Enter name separated by commas - ")
list1 = names.split(",")          # Split fn splits the string by the condition like ","

print(list1)

random1 = random.randint(0, (len(list1)-1))
print("The person to pay the bill is ", list1[random1])
