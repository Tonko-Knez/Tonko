list = [[8,9,10,11,12,13,14,15],[4,5,6,7,12,13,14,15],[2,3,6,7,10,11,14,15],[1,3,5,7,9,11,13,15]]

step = 0
count = 0

print('Imagine number between 1-15')


while step < len(list):
    answer = input("Is imagined number in this list? " + str(list[step])+'\n')
    if answer == "yes":
        count+=list[step][0]
        step+=1
    elif answer == "no":
        step+=1
    else:
        print('Please answer with "yes" or "no"!')
        
    
print("Your number is number "+str(count)+'!')
    
