import random

choice=['rock','paper','scissors']

def rps():
    tries=1
    print("Welcome to Rock, Paper, Scissors!")
    while True:

        if tries>3:
            play_again=input("Do you want to play again? (yes/no): ").lower()
            if play_again !='yes':
                print("Thanks for playing! Goodbye!")
                break
        
        user_choice=input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in choice:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return

        computer_choice=random.choice(choice)
        print(f"Computer chose: {computer_choice}")

        if user_choice==computer_choice:
            print("It's a tie!")
        elif (user_choice=='rock' and computer_choice=='scissors') or \
             (user_choice=='paper' and computer_choice=='rock') or \
             (user_choice=='scissors' and computer_choice=='paper'):
            print("You win!")
        else:
            print("You lose!")

        tries+=1

rps()