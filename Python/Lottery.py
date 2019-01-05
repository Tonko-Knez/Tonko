# Lottery simulation

import random


winning_combination = []

def lottery():
   
    number = 0
    list_of_balls = list(range(1,45))
    

        
    while number < 7:
            ball = random.choice(list_of_balls)
            winning_combination.append(ball)
            list_of_balls.remove(ball)
            
    
            number+=1
    else:
        return list_of_balls
       
          
            
               
    
list_of_balls = lottery()    


print("The lucky combination is",winning_combination)
