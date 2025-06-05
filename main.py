from intro import intro
from guess import think_of_number, display_attempts_left, make_guess, check_guess

def main():
    sphinx_number = think_of_number()
    end_game = False
    attempts_left = intro()
    display_attempts_left(attempts_left)
    user_guess = make_guess()
    attempts_left, end_game = check_guess(user_guess, sphinx_number, attempts_left)
    


if __name__ == "__main__":
    main()