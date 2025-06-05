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