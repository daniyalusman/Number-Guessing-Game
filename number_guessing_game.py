import random
winning_number = random.randint(1, 100)
guess = 1
game_over = False
guess_number = int(input("Guess a number: "))

while not game_over:
    if guess_number == winning_number:
        print(f"You win and you guess {guess} times.")
        game_over = True
    else:
        if guess_number < winning_number:
            print("Too low")
        else:
            print("Too high")
        guess_number = int(input("Guess Again: "))
        guess += 1