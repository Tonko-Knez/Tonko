# Throw 5 dices until all of dices show same value. Print the result and number of tries.


import random

list = []

def dice_throw():
    number = random.randint(1,6)
    return number



def n_dices(n):
       
        for number in range(n): 
            list.append(dice_throw())
            list.sort()



def dices():
    tries  = 0
    while True:
        list[:] = []
        n_dices(5)
        tries+=1
        if list[0] == list[4]:
            print(list)
            print("Number of tries:",tries)
            break
  
        
dices()
        
