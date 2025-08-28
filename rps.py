import random

choice=['rock','paper','scissors']

def rps():
    tries=1
    round=1
    win=0
    print("Welcome to Rock, Paper, Scissors!")
    while True:

        if tries>3:
            play_again=input("Do you want to play again? (yes/no): ").lower()
            round+=1
            tries=1
            if play_again !='yes':
                print("Thanks for playing! Goodbye!")
                print(f"You won {win} out of {round} rounds.")
                break
        
        user_choice=input("Enter your choice (rock, paper, scissors) or 'quit' to Exit: ").lower()
        if user_choice not in choice and user_choice !='quit':
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice=random.choice(choice)
        print(f"Computer chose: {computer_choice}")

        if user_choice==computer_choice:
            print("It's a tie!")
        elif (user_choice=='rock' and computer_choice=='scissors') or \
             (user_choice=='paper' and computer_choice=='rock') or \
             (user_choice=='scissors' and computer_choice=='paper'):
            print("You win!")
            win+=1
        elif user_choice=='quit':
            print("Thanks for playing! Goodbye!")
            print(f"You won {win} out of {round} rounds.")
            break
        else:
            print("You lose!")

        tries+=1

rps()