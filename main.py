from intro import intro
from guess import think_of_number, display_attempts_left, make_guess

def main():
    sphinx_number = think_of_number()
    end_game = False
    attempts_left = intro()
    display_attempts_left(attempts_left)
    user_guess = make_guess()
    end_game = check
    


if __name__ == "__main__":
    main()