import random

def age_prediction_game ():
    # how much will the user bet
balance = float(input("How much will you bet!: $"))

# now we gotta make sure the game keeps running as long as the player has money in their balance
while balance > 0:
    # random number between 1 and 10
        random_int = random.randint(1, 10)
        guesses = 0
        max_guesses = 3
        # player gets max 3 guesses

        while guesses < max_guesses:
            guess = int(input("Guess the number (between 1 and 10): "))
            guesses += 1    # adding a guess to the guess count tally
                        
            if guess == random_int:
                print("You hit the jackpot 🎰, you get to win $100!")
                balance += 100
                break
            # if they get it on the first try, they win big, jackpot!

            elif guess > random_int:
                print("The number you have selected is higher than the actual number.")
            else:
                print("The number you have selected is lower than the actual number.")
                # if they guess wrong of course

             if guesses == max_guesses:
                print("You've used all your guesses. Charging a $25 penalty.")
                balance -= 25
                # this is what happens when you bet, you lose money!! dont do it! anyways, here is the penalty in game

            if guess != random_int:
            print("Sorry, you didn't guess the number. Deducting $50.")
            balance -= 50

                # Display the player's current balance
        print(f"Your current balance is: ${balance}")
        
        if balance <= 0:
            print("Your broke!")
            choice = input("Do you want to add more money or do the smart thing and save your money for rainy days? Type 'im an idiot' to add more money or 'quit' to quit: ").strip().lower()
# strip helps remove spaces from user input
# lower converts user input to lower case
        if choice == 'add':
                additional_money = float(input("Enter your bet!: $"))
                balance += additional_money

        elif choice == 'quit':
                print("Smart move, go home.")
                break