# Import the required module
import unittest
from guess_the_number import GuessTheNumberGame  # Import the game class

# Create a class to test the game
class TestGuessTheNumber(unittest.TestCase):

    # Test the function that generates a secret number
    def test_generate_random_number(self):
        # Create a game object
        game = GuessTheNumberGame()
        
        # Generate a secret number
        number = game.generate_random_number()
        
        # Check if the number is made of digits and has 4 digits
        self.assertTrue(number.isdigit())
        self.assertEqual(len(number), 4)

    # Test the function that provides clues for guesses
    def test_get_clues(self):
        # Create a game object
        game = GuessTheNumberGame()
        
        # Set the secret number for testing
        game.secret_number = "1234"
        
        # Check clues for different guesses
        self.assertEqual(game.get_clues("5678"), "")  # No correct digits
        self.assertEqual(game.get_clues("1243"), "circle x x")  # 1 digit right place, 2 digits wrong place
        self.assertEqual(game.get_clues("4321"), "x x x x")  # All digits correct, but in different places

# Start testing
if _name_ == "_main_":
    unittest.main()  # Run the tests