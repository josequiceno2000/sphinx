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