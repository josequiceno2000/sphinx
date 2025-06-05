import random

def display_attempts_left(attempts_left: int) -> None:
    """
    Displays the current number of attempts left.
    """

    print("\n********** ATTEMPTS LEFT **********\n")
    print(f"You have {attempts_left} guesses remaining.".center(35))
    print("\n***********************************\n")

def think_of_number():
    """
    Returns a random number between 1 and 100.
    """

    return random.randint(1, 100)

def check_guess(user_guess: int, sphinx_number: int, attempts_left: int) -> bool:
    """
    Checks if user guess is too high, too low, or correct, then returns adjusted attempts_left and bool for end_game.
    """

    if user_guess == sphinx_number:
        print(f"You got it! The answer was {sphinx_number}.")
        return (attempts_left, True)
    elif user_guess > sphinx_number:
        print("Too high.")
        attempts_left -= 1
    elif user_guess < sphinx_number:
        print("Too low.")
        attempts_left -= 1

    if attempts_left == 0:
        return (attempts_left, True)
    return (attempts_left, False)

def make_guess() -> int:
    """
    Returns user guess as long as it is a number between 1 and 100 (inclusive).
    """

    user_guess = 0
    while (not isinstance(user_guess, int)) or (user_guess < 1) or (user_guess > 100):
        try:
            user_guess = int(input("Make a guess.\n> "))
        except ValueError:
            print("\n******************** ERROR ********************\n")
            print("You must type a number ('1', '12', etc.)".center(47))
            print("\n***********************************************\n")
    
    return user_guess