import random

def determine_winner(user, bot):
    if user == bot:
        return "tie"
    win_conditions = {
        "rock": "scissor",
        "paper": "rock",
        "scissor": "paper"
    }
    if win_conditions[user] == bot:
        return "user"
    else:
        return "bot"

def game():
    choices = ["rock", "paper", "scissor"]
    user_score = 0
    bot_score = 0

    while True:
        user_choice = input("Enter your move (Rock, Paper, Scissor) or 'exit' to quit: ").lower()
        if user_choice == "exit":
            print(f"Final Score - You: {user_score}, Bot: {bot_score}")
            if user_score > bot_score:
                print("You Won!")
            elif user_score < bot_score:
                print("Bot Won!")
            else:
                print("Match Tie!")
            break

        if user_choice not in choices:
            print("Invalid choice, try again!")
            continue

        bot_choice = random.choice(choices)
        print(f"You chose: {user_choice}, Bot chose: {bot_choice}")

        winner = determine_winner(user_choice, bot_choice)
        if winner == "tie":
            print("It's a tie! No points.")
        elif winner == "user":
            user_score += 1
            print("You get +1 point!")
        else:
            bot_score += 1
            print("Bot gets +1 point!")

if __name__ == "__main__":
    game()
