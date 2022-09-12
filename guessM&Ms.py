import random


def guessing_game():

    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")

    mnms = random.randint(1, 100)

    attemptLimit = 10 
    attempts = 0

    while attempts < attemptLimit:

        guess = int(input("How many M&Ms there are in the jar? "))
        attempts += 1

        if guess == mnms:
            print(f"correct! there are {mnms} M&Ms") 
            break
        elif guess > mnms:
            if guess - mnms >= 15:
                print("that is way too much, try again")
            elif guess - mnms < 15:
                print("that is too much, try again")
        else:
            if mnms - guess >= 15:
                print("that is way too low, try again")
            elif mnms - guess < 15:
                print("that is low, try again")
            
            
    if attempts > attemptLimit:
        print("you are out of tries rip bozo")    

if __name__ == "__main__":
    guessing_game()
