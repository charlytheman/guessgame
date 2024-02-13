import random

# Define constants
MAX_LEVEL = 5  # Maximum number of levels in the game
MAX_GUESSES = 3  # Maximum number of guesses per level

# Define variables
score = 0  # Player's score
high_scores = []  # List of high scores

# Define functions

def get_player_name():
    """Ask the player for their name and return it as a string."""
    name = input("Enter your name: ")
    return name

def display_high_scores():
    """Display the list of high scores."""
    print("High Scores:")
    for i, score in enumerate(high_scores):
        print(i+1, ".", score[0], "-", score[1], "points")
        
def play_game():
    """Play one round of the game."""
    global score
    level = 1  # Start at level 1
    
    while level <= MAX_LEVEL:  # Loop through all levels
        print("Level", level)
        print("--------------")
        max_number = 10 * level  # Calculate the maximum number for this level
        print(f"The secret number is between 1 and {max_number}.")  # Display the range of numbers
        secret_number = random.randint(1, max_number)  # Generate a new secret number for each level
        guesses_left = MAX_GUESSES  # Reset the number of guesses for each level
        
        while guesses_left > 0:  # Loop until the player runs out of guesses
            print("Guesses left:", guesses_left)
            guess = int(input("Enter your guess: "))  # Ask the player for a guess
            
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print("Congratulations! You guessed the number.")
                points = guesses_left * level  # Calculate the number of points the player earned
                score += points  # Add the points to the player's score
                print("You earned", points, "points!")
                break
                
            guesses_left -= 1  # Decrement the number of guesses left
            
        if guesses_left == 0:  # If the player ran out of guesses, reveal the secret number
            print("Sorry, you ran out of guesses. The number was", secret_number)
            
        level += 1  # Move on to the next level
        
    print("Game over!")
    print("Score:", score)
    high_scores.append((get_player_name(), score))  # Add the player's score to the list of high scores
    high_scores.sort(key=lambda x: x[1], reverse=True)  # Sort the high scores in descending order
    display_high_scores()  # Display the list of high scores

# Main program

print("Welcome to Guess the Number!")
play_again = "yes"

while play_again.lower() == "yes":  # Loop until the player decides to quit
    score = 0  # Reset the player's score
    play_game()  # Play one round of the game
    play_again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing!")


