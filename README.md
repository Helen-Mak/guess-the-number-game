# Guess the Number Game

This is a simple "Guess the Number" game implemented in Python. The computer generates a random number within a chosen range, and the player tries to guess it. The game provides feedback on whether the guess is too high or too low and keeps track of the number of attempts. The game also features basic localization for English, German, and Russian languages.

## Features

* **Interactive Gameplay:** A classic "Guess the Number" experience with clear prompts and feedback.
* **Range Selection:** Players can define the minimum and maximum numbers for the guessing range.
* **Attempt Tracking:** The game counts and displays the number of attempts made by the player.
* **Best Score:** Keeps track of the player's best (lowest) number of attempts across multiple games.
* **Language Localization:** Supports English (en), German (de), and Russian (ru) languages. The game prompts the user to choose their preferred language at the start.
* **Input Validation:** Handles non-numeric input and out-of-range guesses gracefully.
* **Range Limitation:** Prevents the guessing range from being excessively large.

## How to Play

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd guess_number_game
    ```
    *(Replace `<repository_url>` with the actual URL of your GitHub repository)*

2.  **Run the Game:**
    ```bash
    python main.py
    ```

3.  **Follow the Prompts:**
    * The game will first ask you to choose your language. Enter `en`, `de`, or `ru`.
    * Next, you'll be prompted to enter the minimum and maximum numbers for the guessing range.
    * The computer will then generate a random number within that range, and you can start guessing.
    * The game will tell you if your guess is too low or too high.
    * Once you guess the correct number, you'll see the hidden number and the number of attempts you made.
    * You'll be asked if you want to play again. Enter `+` (yes) or `-` (no).

## Project Structure

    guess_number_game/
    ├── logic/
    │   └── game_logic.py     # Contains the core game logic.
    ├── localization.py       # Handles language selection and loading.
    ├── locales/
    │   ├── en.json           # English language messages.
    │   ├── de.json           # German language messages.
    │   └── ru.json           # Russian language messages.
    └── main.py               # The main entry point of the game.
    └── README.md             # This file.

## Dependencies

This game is implemented in pure Python and has no external dependencies. You only need a Python interpreter (version 3.6 or higher is recommended) to run it.

## Localization

The game supports localization for English, German, and Russian. All language-specific messages are stored in JSON files within the `locales` directory. The `localization.py` script handles the selection of the language and loading the appropriate messages.

To add support for more languages:

1.  Create a new JSON file (e.g., `es.json` for Spanish) in the `locales` directory.
2.  Copy the structure from one of the existing JSON files and translate the messages into the new language.
3.  Update the `SUPPORTED_LANGUAGES` list in `localization.py` to include the new language code (`"es"`).
4.  Modify the `choose_language()` function in `localization.py` to include the new language option in the prompt.

## Contributing

Contributions to this project are welcome! If you have any ideas for improvements, bug fixes, or new features (like adding more languages), feel free to:

1.  Fork the repository.
2.  Create a new branch for your changes.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## Author

Helen-Mak

## License

This project is licensed under the MIT License. See the LICENSE file for details. 