




import random
from operator import truediv

WORDS = {
    "animals" : ["monkey","turtle","whale","horse","shark","goldfish","lizard"],
    "food" :  ["pizza","sushi","noodles","pretzel","sandwich","cookie","donut"],
    "sports" : ["basketball","football","baseball","golf","skiing","soccer","swimming"]
}



DIFFICULTIES = {
    "easy": 10,
    "medium": 8,
    "hard": 6
}
def get_word(category):
    """
    Picks a random secret word from the specified category.
    """
    if category in WORDS:
        return random.choice(WORDS[category])


def start_game():
    """
    difficulty and category selection.
    """
    print("Welcome to the Console Word Guesser!")
    # Difficulty selection
    while True:
        level = input(f"Choose difficulty (Easy: 10 tries, Medium: 8 tries, Hard: 6 tries): ").lower().strip()
        if level in DIFFICULTIES:
            initial_tries = DIFFICULTIES[level]
            print(f"Starting with {initial_tries} tries.")
            break
        print("Invalid difficulty choice. Please type 'easy', 'medium', or 'hard'.")

    # Category selection
    available_categories = ", ".join(WORDS.keys())
    while True:
        category = input(f"Choose a category ({available_categories}): ").lower().strip()
        if category in WORDS:
            break
        print(f"Invalid category choice. Please choose from: {available_categories}")

    return initial_tries, category


def get_valid_guess(guessed_letters):
    """
    Ask user for a single letter guess and validates the input.
    Returns: The valid, lowercase, unguessed letter.
    """
    while True:
        guess = input("Enter a single letter guess: ").lower().strip()

        if not guess:
            print("Input cannot be blank. Please enter a letter.")
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter only a single letter (a-z).")
            continue

        if guess in guessed_letters:
            # Non-penalizing repeat warning
            print(f"You already guessed '{guess}'. Please try a new letter.")
            continue

        return guess


def display_game_state(secret_word, guessed_letters, remaining_tries):
    """
    Prints the current state of the game:
     The masked word
     Remaining tries
     Sorted list of already guessed letters.
    """
    # Getting masked word with spaces
    masked_word_list = [
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    ]
    masked_word_display = " ".join(masked_word_list)

    # Print feedback
    print("-" * 40)
    print(f"Word Progress: {masked_word_display}")
    print(f"Tries Remaining: {remaining_tries}")
    print(f"Guessed Letters (Sorted): {', '.join(sorted(guessed_letters))}")
    print("-" * 40)





# --- 3. Round and Main Game Flow Functions ---

def play_round(initial_tries, category):
    """
    The main game loop for one round.
    Returns: True if the player won, False otherwise.
    """
    secret_word = get_word(category)
    guessed_letters = []
    remaining_tries = initial_tries
    win = False

    print(f"\n--- NEW GAME STARTED (Category: {category.title()}) ---")

    # The game loop continues until the word is revealed or tries run out
    while remaining_tries > 0:
        display_game_state(secret_word, guessed_letters, remaining_tries)

        # Check for win condition
        if all(letter in guessed_letters for letter in set(secret_word)):
            win = True
            break

        # Get and process the guess
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"SUCCESS! The letter '{guess}' is in the word.")
        else:
            remaining_tries -= 1
            print(f"INCORRECT! The letter '{guess}' is NOT in the word. You lose 1 try.")

    # Game end summary
    print("\n" + "=" * 40)
    final_word_display = f"The secret word was: {secret_word.upper()}"

    if win:
        # Final display state (showing the fully revealed word)
        display_game_state(secret_word, guessed_letters, remaining_tries)
        print(f"CONGRATULATIONS! You guessed the word!")
        print(final_word_display)
        return True
    else:
        # Final display state (showing all letters tried and 0 tries left)
        display_game_state(secret_word, guessed_letters, 0)
        print("GAME OVER! You ran out of tries.")
        print(final_word_display)
        return False


def main_game():
    """
    Runs the overall game, tracking scores and managing the play-again loop.
    """
    total_wins = 0
    total_losses = 0
    play_on = True

    # Get start settings before the loop starts
    initial_tries, category = start_game()

    while play_on:
        # Use settings from setup, but let the user select new ones later if they want a new difficulty/category
        if play_round(initial_tries, category):
            total_wins += 1
        else:
            total_losses += 1

        # Display current score
        print(f"\n[CURRENT SCORE] Wins: {total_wins} | Losses: {total_losses}")
        print("=" * 40)

        # Ask to play again
        while True:
            choice = input("Play again? (y/n): ").lower().strip()
            if choice == 'n':
                play_on = False
                print(f"Thanks for playing! Final Score: Wins = {total_wins}, Losses = {total_losses}")
                break
            elif choice == 'y':
                # Re-start settings for the next round
                initial_tries, category = start_game()
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    # Call the main function to start the game
    main_game()








