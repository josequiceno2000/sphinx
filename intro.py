title_card = """
   ▄████████    ▄███████▄    ▄█    █▄     ▄█  ███▄▄▄▄   ▀████    ▐████▀ 
  ███    ███   ███    ███   ███    ███   ███  ███▀▀▀██▄   ███▌   ████▀  
  ███    █▀    ███    ███   ███    ███   ███▌ ███   ███    ███  ▐███    
  ███          ███    ███  ▄███▄▄▄▄███▄▄ ███▌ ███   ███    ▀███▄███▀    
▀███████████ ▀█████████▀  ▀▀███▀▀▀▀███▀  ███▌ ███   ███    ████▀██▄     
         ███   ███          ███    ███   ███  ███   ███   ▐███  ▀███    
   ▄█    ███   ███          ███    ███   ███  ███   ███  ▄███     ███▄  
 ▄████████▀   ▄████▀        ███    █▀    █▀    ▀█   █▀  ████       ███▄ 
                                                                        
"""
def choose_difficulty() -> str:
    player_difficulty = ""

    while player_difficulty not in (["hard", "easy"]):
        if player_difficulty != "":
            print("\nINVALID: you must type either 'easy' or 'hard'\n")
        player_difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.\n> ").lower()
    
    return player_difficulty

def intro() -> str:
    """Prints title card and welcome messages to begin game."""
    print(title_card)
    print("Welcome to SPHINX. Try to guess the number in my head...")
    print("I'm thinking of a number between 1 and 100.")

