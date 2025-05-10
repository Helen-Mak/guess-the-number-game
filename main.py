# Import game logic module
from logic import game_logic

# Import localization functions
from localization import choose_language, get_localized_messages

# Determine the user's language preference
selected_language = choose_language()

# Load the messages for the selected language
messages = get_localized_messages(selected_language)

# Set the loaded messages in the game logic module
game_logic.set_language(messages)

# Get the player's name using the localized greeting
name = input(f"{messages['hello_name_prompt']}\n")

# Print a personalized greeting
print(f"\n{messages['nice_to_meet_you']}, {name}!")

# Initialize the game counter
games_count = 0

# Main game loop
while True:

    # Increment the game counter
    games_count += 1
    # Start a new game
    game_logic.start_game()

    # Loop to ask if the player wants to play again
    while True:
        answer = input(f"\n{messages['play_again']}\n").lower()

        # If the player answers "yes", break the inner loop to start a new game
        if answer == "+":
            break
        # If the player answers "no", print the thank you message and exit
        elif answer == "-":
            print(f"\n{messages['thank_you']}\n{messages['games_played'].format(count=games_count)}\n{game_logic.best_counter()}")
            exit()
        # If the input is invalid, show an error message
        else:
            print(f"\n{messages['invalid_input']}.")
