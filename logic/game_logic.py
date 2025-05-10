import random

# Variable to store the best result (fewest attempts)
best_result = None
# Variable to hold the localized messages
localized_messages = None


# Function to set the localized messages for the current game
def set_language(messages):
    global localized_messages
    localized_messages = messages


# Function to start a new game
def start_game():
    # Inform the player about choosing the range
    print(localized_messages["choose_range"])

    # Loop to get valid range input from the player
    while True:
        try:
            # Get the minimum and maximum numbers for the guessing range
            start = int(input(localized_messages["enter_min"]))
            finish = int(input(localized_messages["enter_max"]))

            # Check if the minimum is greater than or equal to the maximum
            if start >= finish:
                print(localized_messages["minimum_greater_than_maximum"])
                continue

            # Check if the range is too large
            if (finish - start) > 1000:
                print(localized_messages["range_too_large"])
                antw = input(f"{localized_messages['change_range_prompt']}\n").lower()
                if antw == "+":
                    continue
                elif antw != "-":
                    print(localized_messages["invalid_input"])
                    continue

            # If the range is valid, break the loop
            break
        except ValueError:
            # Handle non-numeric input
            print(localized_messages["only_numbers"])

    # Generate a random number within the chosen range
    number = random.randint(start, finish)
    print(localized_messages["guess_number"].format(start=start, finish=finish))

    # Initialize the attempts counter
    attempts = 0

    # Main guessing loop
    while True:
        try:
            # Get the player's guess
            guess = int(input(localized_messages["enter_guess"]))
            # Increment the attempts counter
            attempts += 1
        except ValueError:
            # Handle non-numeric input
            print(localized_messages["only_numbers"])
            continue

        # Check if the guess is outside the allowed range
        if guess < start or guess > finish:
            print(localized_messages["out_of_range"].format(start=start, finish=finish))
            continue

        # Provide feedback on the guess
        if guess < number:
            print(localized_messages["too_low"])
        elif guess > number:
            print(localized_messages["too_high"])
        # If the guess is correct
        else:
            print(localized_messages["success"].format(number=number, attempts=attempts))
            # Update the best result
            update_best_result(attempts)
            # Break the guessing loop
            break


# Function to update the best result
def update_best_result(attempts):
    global best_result
    if best_result is None or attempts < best_result:
        best_result = attempts


# Function to return the best score message
def best_counter():
    if best_result is not None:
        return localized_messages["best_score"].format(best=best_result)
    return localized_messages["no_record"]
