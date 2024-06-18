import random

def age_prediction_game():
    # the users bet
    balance = float(input("How much will you bet!: $"))
    
    # game will keep running so long as the user has money
    while balance > 0:
        # Generate a random number between 1 and 10
        random_int = random.randint(1, 10)
        guesses = 0
        max_guesses = 3
        
        # Allow the player up to 3 guesses
        while guesses < max_guesses:
            guess = int(input("Guess the number (between 1 and 10): "))
            guesses += 1    # adding a guess to the guess count tally
            
            if guess == random_int:
                print("You hit the jackpot 🎰, you get to win $100!")
                balance += 100
                break  # Exit the loop if the player guesses correctly
            elif guess > random_int:
                print("The number you have selected is higher than the actual number.")
            else:
                print("The number you have selected is lower than the actual number.")
            
            # if they guess wrong of course
            if guesses == max_guesses:
                print("You've used all your guesses. gimme 25 big guy.")
                balance -= 25
        
        if guess != random_int:
            print("Sorry, you didn't guess the number. 50's in palm. Now.")
            balance -= 50

        # Display the player's current balance
        print(f"Your current balance is: ${balance}")
        
        if balance <= 0:
            print("Your broke!")
            choice = input("Do you want to add more money or do the smart thing and save your money for rainy days? Type 'add' to add more money or 'quit' to quit: ").strip().lower()
            if choice == 'add':
                additional_money = float(input("Enter your bet!: $"))
                balance += additional_money
            elif choice == 'quit':
                print("Smart move, go home.")
                break
        else:
            # ask the player if they want to play again
            play_again = input("Do you want to play again? Type 'yes' to play again or 'no' to quit: ").strip().lower()
            if play_again != 'yes':
                print("Thank you for playing! Goodbye.")
                break  # Exit the main game loop if the player chooses not to play again

# code will only run if the script is executed directly, not if it is imported as a module
if __name__ == "__main__":
    age_prediction_game()
