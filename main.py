import random
import time

def randomNumber():
    return random.randint(1, 100)

def user_input():
    time.sleep(1/2)
    while True:
        try:
            user_inp = int(input(f"Enter a number to start the game or enter '0' to exit the program.\n>> "))
            break
        except ValueError:
            print("Error 404: Invalid input, please try again.")
            time.sleep(1/2)
    time.sleep(1/2)
    if user_inp == 0:
        print("Exiting the program...")
        time.sleep(1/4)
        exit()
    return user_inp

def core(tries, number):
    print("\nYou have 30 tries to guess a number from 1-100.")
    while tries > 0:
        guess = user_input()
        print(f"Attempt counter: {31 - tries}")
        time.sleep(1/4)
        if guess < number:
            print("-> Go higher!!!")
        elif guess > number:
            print("-> Go lower!!!")
        else:
            print(f"Congrats!! You did it, {guess} was the correct number, it took you {31 - tries} tries!!")
            break
        tries -= 1
    else:
        print("Sorry, you ran out of chances :(")
        exit()

def main():
    number = randomNumber()
    tries = 30
    core(tries, number)

if __name__ == "__main__":
    main()
