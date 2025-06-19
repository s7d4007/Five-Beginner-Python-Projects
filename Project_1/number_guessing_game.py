import random

def guess_num():
    
    # The computer chooses a random number 
    # between the range specified in the parenthesis. 
    # Here, the range is 1-100
    number = random.randint(1,100)
    
    print("----------------Number Guessing Game----------------")
    print("Choose a number between 1 to 100.")
    guessed_num = int(input())
    
    #Verify if the number chose by the computer and the user matches.
    #If match is found, print Won, Otherwise print lose.
    
    if guessed_num == number:
        print("Congratulations!, You guessed the correct number.")
    elif abs(guessed_num - number) <= 10:
        print("You are close !!! Let's take one more try.") #If the user is close by 10 numbers, give them a second chance.
        print("Choose a number between 1 to 100.")
        guessed_num = int(input())
        if guessed_num == number:
            print("Congratulations!, You guessed the correct number.")
        else:
            print(f"Sorry, you have guessed the wrong number.\n The correct number is {number}")
    else:
        print(f"Sorry, you have guessed the wrong number.\n The correct number is {number}")
        
guess_num()