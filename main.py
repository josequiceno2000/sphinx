from intro import intro
from guess import display_attempts_left, think_of_number

def main():
    sphinx_number = think_of_number()
    correct_guess = False
    attempts_left = intro()
    display_attempts_left(attempts_left)
    


if __name__ == "__main__":
    main()