import random

def display_attempts_left(attempts_left: int) -> None:
    """
    Displays the current number of attempts left.
    """

    print("\n********** ATTEMPTS LEFT **********")
    print(f"\nYou have {attempts_left} guesses remaining.\n".center(35))
    print("***********************************")

def think_of_number():
    """
    Returns a random number between 1 and 100.
    """

    return random.randint(1, 100)

def make_guess() -> int:
    """
    Returns user guess as long as it is a number between 1 and 100 (inclusive).
    """

    user_guess = 0
    while (not isinstance(user_guess, int)) and (not 1 <= user_guess <= 100):
        try:
            user_guess = int(input("Make a guess.\n> "))
        except TypeError:
            print("ERROR: you must type a number ('1', '12', etc.)")
    
    return user_guess