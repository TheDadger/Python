import random

def guess_game():
    num=random.randint(1, 20)
    guess=None
    tries=0
    max_tries=int(input("Enter the number of tries you want: "))

    while guess!=num and tries<max_tries:
        guess=int(input("Enter your guess between 1 to 20: "))
        tries+=1
        if guess<num:
            print("Your guess is too low")
        elif guess>num:
            print("Your guess is too high")
        else:
            print(f"Congratulations! You guessed the number {num} in {tries} tries.")
            break
    if tries==max_tries and guess!=num:
        print(f"Sorry, you've used all your tries. The number was {num}. Better luck next time!")

while True:
    guess_game()
    repeat=input("Do you want to play again? (y/n): ").lower()
    if repeat!='y':
        print("Thank you for playing! Goodbye!")
        break
