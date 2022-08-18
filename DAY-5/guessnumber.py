
import random


n= random.randint(1,10)
count=0
while n!= "guess":
    if count == 3 :
        print('you falied to guess')
        break
    guess = int(input('enter the number betwwen 1 to 10: '))
    if guess < n :
        print('better luck next time')
    elif guess > n :
        print('congratulation')
    else :
        print('you have guessed it !')
        break
    count += 1
    
     

    