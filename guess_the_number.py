"""HafeezUllah"""

import random # We need the 'random' module to generate random numbers

class GuessTheNumberGame:
    def __init__(self):
        self.secret_number = self.generate_random_number()
        # Start the game by creating a secret number

    def generate_random_number(self):
         # This function generates a random 4-digit number for the game
        return str(random.randint(1000, 9999))

    def get_clues(self, guess):
        # This function calculates the clues for the player's guess
        clues = []
        for i in range(4):
            if guess[i] == self.secret_number[i]:
                clues.append("circle") # If the digit is correct and in the right spot
            elif guess[i] in self.secret_number:
                clues.append("x")# If the digit is correct but in the wrong spot
            else:
                clues.append("") # If the digit is not correct
        return " ".join(clues) # Combine the clues into a single message

    def play(self): 
        print("Welcome to Guess the Number!")

        play_again = True
        while play_again:
            attempts = 0

            while True:
                player_guess = input("Enter your 4-digit guess (or 'q' to quit): ")

                if player_guess.lower() == 'q':
                    print("Thanks for playing!")
                    break

                if len(player_guess) != 4 or not player_guess.isdigit():
                    print("Invalid input. Please enter a 4-digit number.")
                    continue

                attempts += 1
                if player_guess == self.secret_number:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                else:
                    clues = self.get_clues(player_guess)
                    print("Clues:", clues)

            play_again_input = input("Do you want to play again? (y/n): ")
            play_again = play_again_input.lower() == 'y'
            if play_again:
                self.secret_number = self.generate_random_number()

if __name__ == "__main__":
    game = GuessTheNumberGame() 
     # Create a new game instance
    game.play() # Start playing the game
