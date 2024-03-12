import random

# Configuration dictionary
game_config = {
    "colors": ["red", "green", "blue", "yellow", "orange", "purple", "black", "white"],
    "num_fields": 3,
    "allow_color_repeats": False,
    "num_possible_colors": 4,
    "max_guesses": 10,
}


def generate_hidden_sequence(config):
    if config["allow_color_repeats"]:
        return [
            random.choice(config["colors"][: config["num_possible_colors"]])
            for _ in range(config["num_fields"])
        ]
    else:
        return random.sample(
            config["colors"][: config["num_possible_colors"]], config["num_fields"]
        )


def play_mastermind(config):
    hidden_sequence = generate_hidden_sequence(config)
    print("\033[90m" + "-" * 66)
    print(
        "\033[92mWelcome to Mastermind! \033[90mTry to guess the hidden sequence of colors."
    )
    print("\033[90m" + "-" * 66)
    print("\033[0mYou have", config["max_guesses"], "attempts to guess the sequence.")
    print(
        "\033[90mThe possible colors are:\033[0m",
        ", ".join(config["colors"][: config["num_possible_colors"]]),
    )
    print(
        "Write '\033[31mcolor\033[0m' or '\033[31mcolors\033[0m' to show the possible colors."
    )
    print("Number of fields:", config["num_fields"])
    print(
        "Write '\033[31mexit\033[0m' or '\033[31mquit\033[0m' or '\033[31mend\033[0m' to exit the game.\n"
    )

    num_guesses = 0

    while num_guesses < config["max_guesses"]:
        guess = (
            input("\033[33mGuess #" + str(num_guesses + 1) + "\033[0m: ")
            .strip()
            .lower()
            .split()
        )

        if not guess:
            print("\033[31mWrite something!\033[0m")
            continue

        if guess[0] in ["exit", "quit", "end"]:
            print("\033[32mThanks for playing!\033[0m")
            break

        if guess[0] in ["color", "colors"]:
            print(
                "\033[90mThe possible colors are:\033[0m",
                ", ".join(config["colors"][: config["num_possible_colors"]]),
            )
            continue

        if len(guess) != config["num_fields"]:
            print(
                f"\033[31mInvalid guess. Please enter {config['num_fields']} colors.\033[0m"
            )
            continue

        feedback = check_guess(hidden_sequence, guess)
        print(f"\033[90mFeedback: {feedback}\033[0m")

        if feedback == ("Black " * config["num_fields"]).strip():
            print(
                "\033[32mCongratulations! You've guessed the correct sequence.\033[0m"
            )
            break

        num_guesses += 1

    if num_guesses == config["max_guesses"]:
        print(
            "\033[31mSorry, you've run out of guesses. The hidden sequence was: ",
            hidden_sequence,
            "\033[0m",
        )


def check_guess(hidden_sequence, guess):
    feedback = ""
    remaining_sequence = []

    for i in range(len(hidden_sequence)):
        if hidden_sequence[i] == guess[i]:
            feedback += "Black "
        else:
            remaining_sequence.append(hidden_sequence[i])

    for color in guess:
        if color in remaining_sequence:
            feedback += "White "
            remaining_sequence.remove(color)

    return feedback.strip()


play_mastermind(game_config)
