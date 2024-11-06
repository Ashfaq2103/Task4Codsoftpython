import random

# Score tracking
user_score = 0
computer_score = 0

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main game function
def play_round():
    global user_score, computer_score
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Ensure valid input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the result
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1

# Main program loop
def play_game():
    global user_score, computer_score
    while True:
        play_round()
        print(f"\nScores => You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play another round
        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == "no":
            print("Thanks for playing!")
            break

# Run the game
play_game()
