#smart menu

import time

print ("welcome to italian restaurant !")
print ("wait a few seconds to scan the menu ! \n")
time.sleep(5)

menu = {"pizza steak" : "20$", "pizza pepperoni" : "10$", "pasta alfredo" : "15$", "pasta shrimp" : "10$"}
print (menu)
order = input ("Do you want to order ? ")
factor = []
while order == "yes" :
    bill1 = 0
    bill2 = 0
    bill3 = 0
    bill4 = 0
    food = input ("Enter your food : ")
    count = int (input ("How many " + food + " do you want ? "))
    if food == "pizza steak" :
        bill1 = count * 20
        factor.append(bill1)
    if food == "pizza pepperoni" :
        bill2 = count * 10
        factor.append(bill2)
    if food == "pasta alfredo" :
        bill3 = count * 15
        factor.append(bill3)
    if food == "pasta shrimp" :
        bill4 = count * 10
        factor.append(bill4)
    order = input ("Do you want to order anything else ? ")

finally_factor = sum(factor)
print ("you have to pay " + str(finally_factor) + "$")
print ("\n")

answer = input ("Do you want to (pay / cancel) ? ")
if answer == "pay" :
    time.sleep(3)
    print ("your order has been registered !")
elif answer == "cancel" :
    time.sleep(3)
    print ("your order has been cancelled !")



#attack on password

import random
password = int (input ("enter a password : "))
guess = 0
while guess != password :
    guess = random.randint(1000,9999)
    print (guess)
print ("The password is " + str(guess))