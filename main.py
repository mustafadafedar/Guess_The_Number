import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the number between 1 and {x}\n"))
        if guess < random_number:
            print("sorry guess again to low.")
        elif guess > random_number:
            print("sorry guess again to high.")
    print(f"yay congrats. you have guessed the number {random_number} correctly!!!")
guess(10)
