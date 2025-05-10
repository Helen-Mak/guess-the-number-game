import json
import os

# Default language code
DEFAULT_LANGUAGE = "en"
# List of supported language codes
SUPPORTED_LANGUAGES = ["en", "de", "ru"]
# Directory where localization files are stored
LOCALIZATION_DIR = "locales"

# Check if the localization directory exists, and create it if not
if not os.path.exists(LOCALIZATION_DIR):
    try:
        os.makedirs(LOCALIZATION_DIR)
    except OSError as e:
        print(f"Error creating directory {LOCALIZATION_DIR}: {e}")
        # If directory creation fails, exit the program
        exit()


# Function to create default localization files if they don't exist
def create_default_localization_file(lang):
    filepath = os.path.join(LOCALIZATION_DIR, f"{lang}.json")
    if not os.path.exists(filepath):
        default_messages = {}

        if lang == "en":
            default_messages = {
                "choose_language_prompt": "Please choose your language:",
                "choose_language_options": "[en] English\n[de] Deutsch\n[ru] Русский",
                "hello": "Hello",
                "nice_to_meet_you": "Nice to meet you",
                "play_again": "Do you want to play again? (+/-)",
                "thank_you": "Thank you for the game!",
                "games_played": "You played {count} times.",
                "best_score": "Your record: {best} attempts.",
                "no_record": "No record set yet.",
                "choose_range": "\nFirst, choose the range in which you want to guess.",
                "enter_min": "Enter the minimum number: ",
                "enter_max": "Enter the maximum number: ",
                "only_numbers": "\nError: You need to enter numbers!",
                "guess_number": "\nI have guessed a random number from {start} to {finish}, try to guess it!",
                "too_low": "\nToo low! Try higher.",
                "too_high": "\nToo high! Try lower.",
                "out_of_range": "\nYou need to enter a number from {start} to {finish}.",
                "success": "\nCongratulations, you guessed it! :)\nThe hidden number: {number}\nAttempts made: {attempts}",
                "minimum_greater_than_maximum": "\nMinimum must be less than maximum!",
                "range_too_large": "\nThis range is too large, the game will be too difficult!",
                "change_range_prompt": "Do you want to change the starting and/or ending number? (+/-)",
                "invalid_input": "\nInvalid input. Please try again."
            }

        elif lang == "de":
            default_messages = {
                "choose_language_prompt": "Bitte wähle deine Sprache:",
                "choose_language_options": "[en] English\n[de] Deutsch\n[ru] Русский",
                "hello": "Hallo",
                "nice_to_meet_you": "Schön dich kennenzulernen",
                "play_again": "Möchtest du noch einmal spielen? (+/-)",
                "thank_you": "Danke für das Spiel!",
                "games_played": "Du hast {count} Mal gespielt.",
                "best_score": "Dein Rekord: {best} Versuche.",
                "no_record": "Noch kein Rekord aufgestellt.",
                "choose_range": "\nWähle zuerst den Bereich, in dem du raten möchtest.",
                "enter_min": "Gib die kleinste Zahl ein: ",
                "enter_max": "Gib die größte Zahl ein: ",
                "only_numbers": "\nFehler: Du musst Zahlen eingeben!",
                "guess_number": "\nIch habe eine Zufallszahl zwischen {start} und {finish} gewählt. Versuche sie zu erraten!",
                "too_low": "\nZu niedrig! Versuche es höher.",
                "too_high": "\nZu hoch! Versuche es niedriger.",
                "out_of_range": "\nDu musst eine Zahl zwischen {start} und {finish} eingeben.",
                "success": "\nHerzlichen Glückwunsch, du hast es erraten! :)\nDie gesuchte Zahl: {number}\nVersuche benötigt: {attempts}",
                "minimum_greater_than_maximum": "\nDas Minimum muss kleiner sein als das Maximum!",
                "range_too_large": "\nDieser Bereich ist zu groß, das Spiel wird zu schwierig!",
                "change_range_prompt": "Möchtest du die Start- und/oder Endzahl ändern? (+/-)",
                "invalid_input": "\nUngültige Eingabe. Bitte versuche es erneut."
            }

        elif lang == "ru":
            default_messages = {
                "choose_language_prompt": "Пожалуйста, выберите язык:",
                "choose_language_options": "[en] English\n[de] Deutsch\n[ru] Русский",
                "hello": "Привет",
                "nice_to_meet_you": "Приятно познакомиться",
                "play_again": "Хочешь сыграть ещё раз? (+/-)",
                "thank_you": "Спасибо за игру!",
                "games_played": "Ты сыграл(а) {count} раз.",
                "best_score": "Твой рекорд: {best} попыток.",
                "no_record": "Рекорд пока не установлен.",
                "choose_range": "\nДля начала выбери диапазон, в котором ты хочешь угадывать.",
                "enter_min": "Введи минимальное число: ",
                "enter_max": "Введи максимальное число: ",
                "only_numbers": "\nОшибка: нужно ввести числа!",
                "guess_number": "\nЯ загадал случайное число от {start} до {finish}, попробуй угадать!",
                "too_low": "\nСлишком мало! Попробуй больше.",
                "too_high": "\nСлишком много! Попробуй меньше.",
                "out_of_range": "\nНужно ввести число от {start} до {finish}.",
                "success": "\nПоздравляю, ты угадал(а)! :)\nЗагаданное число: {number}\nСделано попыток: {attempts}",
                "minimum_greater_than_maximum": "\nМинимум должен быть меньше максимума!",
                "range_too_large": "\nЭто очень большой диапазон, игра получится слишком сложной!",
                "change_range_prompt": "Хочешь поменять стартовое и/или конечное число? (+/-)",
                "invalid_input": "\nНекорректный ввод. Пожалуйста, попробуй снова."
            }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(default_messages, f, ensure_ascii=False, indent=4)


# Create default localization files if they don't exist
for lang in SUPPORTED_LANGUAGES:
    create_default_localization_file(lang)


# Function to load language-specific messages from a JSON file
def load_language(lang_code):
    filepath = os.path.join(LOCALIZATION_DIR, f"{lang_code}.json")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: Language file for '{lang_code}' not found. Loading default language '{DEFAULT_LANGUAGE}'.")
        return load_language(DEFAULT_LANGUAGE)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filepath}'. Loading default language '{DEFAULT_LANGUAGE}'.")
        return load_language(DEFAULT_LANGUAGE)


# Function to let the user choose the language
def choose_language():
    default_messages = load_language(DEFAULT_LANGUAGE)
    print(default_messages["choose_language_prompt"])
    print(default_messages["choose_language_options"])
    while True:
        choice = input("Enter language code (en, de, ru): ").lower()
        if choice in SUPPORTED_LANGUAGES:
            return choice
        else:
            print("Invalid language code. Please choose from en, de, or ru.")


# Function to get the localized messages for a given language code
def get_localized_messages(lang_code):
    return load_language(lang_code)
