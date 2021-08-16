import random

print("Guess The Number Game\
    \n=====================\n\n\
Instruction :\nGuess a random number beetween 1 to 100.\n\
You can attempt as many times as you want.\nEnjoy!\n")

random_number = random.randint(1, 100)
guess = 0
guess_counter = 0

while guess != random_number:
    guess = int(input("Guess a Number : "))
    if guess < random_number:
        print("Guessed number is too Low. Try Again!!!")
    elif guess > random_number:
        print("Guessed number is too High. Try Again!!!")
    guess_counter += 1
    
print(f"\nCongratulations!!!\nYou found the correct number in {guess_counter} attemps.\n\
The Correct Number was {random_number}.\nYou Win!!!\n")
