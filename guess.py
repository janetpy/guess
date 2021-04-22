import random

print("Welcome to 'guess the number' game")
print("Hello am thinking of a number between 1 and 20")
number= random.randint(1, 20)

try:
    for guesstaken in range (1, 6):

        guess = int(input("Take your guess"))

        if guess > number:
            print("Your guess is greater than the number")
        elif guess < number:
            print("Your guess is smaller than the number")
        else:
            break

    if guess == number:
            print("waw! you guessed right after %s trials" %str(guesstaken))
    else:
            print("You ran out of lives. The number is %s" %str(number))

except:
    print("You need to enter a number")
