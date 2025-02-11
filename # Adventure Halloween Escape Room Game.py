# Adventure Halloween Escape Room Game

room_data = {
    "game room": {
        "description": "Welcome to the Spooky House Escape Room Game, a piano and a locked Door A.",
        "puzzle":"What should I do?",
        "items": [{"piano": "key_A"}, "couch"],
        "doors": {"Door A": "locked"}
    },
    "bedroom 1": {
        "description": "You are in Bedroom 1. You see a queen bed, Door B, and Door C.",
        "items": ["queen bed", "key_B"],
        "doors": {"Door B": "locked", "Door C": "locked"}
    },
    "bedroom 2": {
        "description": "You're in Bedroom 2. You see a double bed, a dresser, and Door B.",
        "items": ["double bed", "key_C", "dresser", "key_D"],
        "doors": {"Door B": "unlocked"}
    },
    "living room": {
        "description": "You're in the living room. You see a dining table, Door C, and Door D.",
        "items": ["dining_table"],
        "doors": {"Door D": "locked"}
    },
    "outside": {
        "description": "You've stepped outside! Congratulations, you have escaped!",
        "items": [],
        "doors": {}
    }
}

# Initialize inventory for the game
inventory = {"keys": [], "name": None, "play": True}

def start_game():
    """Function to start the game and transition to the game room."""
    print("Welcome to the Adventure Game!")
    print("You find yourself waking up in an unfamiliar room... The air feels heavy, and a strange silence fills the space.")
    print("Your mission is to find keys and solve puzzles to escape the rooms. Let's begin.")
    gameroom()

def gameroom():
    """Function for the game room."""
    print("\nLet the game begin!")
    name = input("What is your name, stranger? ")
    inventory["name"] = name  # Store name directly in the inventory dictionary
    print(f"As your eyes adjust, {name}, you see a grand piano, an old couch, and a door marked 'Door A' with a large lock.")

    while inventory["play"]:
        print("\nWhat would you like to do?")
        print("1 - Search for the key")
        print("2 - Exit")
       
        action = int(input("Choose an action (1 or 2): "))

        if action == 1:
            explore_game_room()
            break
        elif action == 2:
            print("An overwhelming sense of dread fills you as you quit the game.")
            inventory["play"] = False
        else:
            print("Invalid action. Try again.")

def explore_game_room():
    """Function to explore the game room."""
    while True:
        print("\nWhere would you like to search?")
        print("1 - Piano")
        print("2 - Couch")

        choice = int(input("Choose an option (1 or 2): "))

        if choice == 1:
            if "key_A" not in inventory['keys']:
                inventory['keys'].append("key_A")
                print("As you lift the piano lid, you find a small, old-fashioned treasure key lying there. It looks like it might open Door A!\n")
                puzzle_gameroom()
                break            
            else:
                print("You've already searched here. The piano holds no more secrets.")
                break
        elif choice == 2:
            print("You lift the cushions, but find nothing but dust. Hahaha!")
        else:
            print("Invalid choice. Please try again.")

    print("Keys in your inventory:", inventory['keys'])

def puzzle_gameroom():
    """Solve puzzle in the game room."""
    print("Decipher the puzzle to unlock Door A")
    while True:
        print("1 - String")
        print("2 - Integer")
        print("3 - Boolean")

        puzzle_answer = input("\nTrue or False represent which type of data in Python? Choose an option (1, 2, or 3): ")

        if puzzle_answer == "3":
            print("\nWell done! You have collected the treasure key.")
            break
        else:
            print("Wrong answer, please try again.")

    while True:
        next_action = input("Would you like to use that treasure key to unlock Door A? (1 - Yes, 2 - No): ")
        if next_action == "1":
            bedroom1()
            break
        elif next_action == "2":
            explore_game_room()
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def bedroom1():
    """Function for Bedroom 1."""
    print("\nYou step through Door A, finding yourself in another dark room.")
    name = inventory["name"]
    print(f"\nCongratulations, {name}! You've moved up to Bedroom 1.")

    print("In this room, you see a grand, old queen bed against one wall, its heavy blankets untouched for years. Two doors stand ahead—Door B and Door C, each locked and silent.")
     
    while True:
        print("\nWhat would you like to do?")
        print("1 - Search for the key")
        print("2 - Exit")
        
        action = int(input("Choose an action (1 or 2): "))

        if action == 1:
            explore_bedroom1()
        elif action == 2:
            print("You decide to exit the game.")
            return
        else:
            print("Invalid action. Please try again.")

def explore_bedroom1():
    """Explore Bedroom 1."""
    while True:
        print("\nWould you like to search the queen bed or explore the room?")
        print("1 - Queen bed")
        print("2 - Explore the room")

        choice = int(input("Choose an option (1 or 2): "))
           
        if choice == 1:
            if "key_B" not in inventory['keys']:
                inventory['keys'].append("key_B")
                print("You lift the dusty blankets and feel around, finally grasping something cold — a key! The tag reads 'Door B!'")
                puzzle_bedroom_1()
                choose_door_bedroom1()
            else:
                print("The bed offers no more secrets; you’ve already claimed its hidden treasure.")
       
        elif choice == 2:
            print("You scan the room, but shadows hold their secrets closely.")
        else:
            print("Invalid choice. Please choose an option (1 or 2).")

    print("Keys in your inventory:", inventory['keys'])

def puzzle_bedroom_1():
    """Solve puzzle for Bedroom 1."""
    print("\nDecipher the puzzle to unlock Door B")
    while True:
        print("1 - #")
        print("2 - //")
        print("3 - /*")

        puzzle_answer = input("\nWhat symbol is used to start a comment in Python? Choose an option (1, 2, or 3): ")

        if puzzle_answer == "1":
            print("\nWell done! You’ve just claimed the hidden treasure key to unlock Door B.")
            return 1
        else:
            print("Wrong answer, please try again.")

def choose_door_bedroom1():
    """Choose which door to unlock in Bedroom 1."""
    while True:
        print("\nTry one of the doors")
        print("1 - Door B")
        print("2 - Door C")

        door_choice = int(input("Choose an option (1 or 2): "))
       
        if door_choice == 1:
            print("You insert the key into Door B, hearing a faint click as it opens...")
            bedroom2()
            break
        elif door_choice == 2:
            print("Sorry, Door C is locked tight, and something tells you this key won’t open it.")
        else:
            print("Invalid choice. Please choose 'Door B' or 'Door C'.")

def bedroom2():
    """Function for Bedroom 2."""
    name = inventory["name"]
    print(f"\nYou've entered Bedroom 2, where a double bed looms in the corner and a dresser stands against a wall stained with blood.")
    print("The air feels thick, and you sense more secrets here. You know that somewhere, there are keys that will lead you closer to freedom.")

    while inventory["play"]:  # Check if the game is still active
        print("\nWhat would you like to do?")
        print("1 - Search for keys")
        print("2 - Exit")
        
        action = int(input("Choose an action (1 or 2): "))

        if action == 1:
            explore_bedroom2()
            if inventory["play"]:  # Check if game is still active after exploring
                bedroom1_return()
        elif action == 2:
            print("An overwhelming sense of dread fills you as you quit the game.")
            inventory["play"] = False  # Set play to False to exit the game
        else:
            print("Invalid action. Try again.")

def explore_bedroom2():
    """Explore Bedroom 2."""
    while True:
        print("\nWould you like to search the double bed or explore the dresser?")
        print("1 - Double bed")
        print("2 - Dresser")

        choice = int(input("Choose an option (1 or 2): "))
        if choice == 1:
            if "key_C" not in inventory['keys']:
                inventory['keys'].append("key_C")
                print("You pull back the bed’s heavy blankets to find a small box hidden underneath. It’s locked. But you have the key now.")
                puzzle_bedroom_2()
                break
            else:
                print("The double bed no longer holds any secrets.")
        elif choice == 2:
            if "key_D" not in inventory['keys']:
                inventory['keys'].append("key_D")
                print("You open the dresser drawer and find a small key hidden inside — this key must open the dresser!")
                break
            else:
                print("The dresser holds no more secrets.")
        else:
            print("Invalid choice. Please select 'Double bed' or 'Dresser'.")

def puzzle_bedroom_2():
    """Solve puzzle for Bedroom 2."""
    print("\nWhat type of puzzle is this?")
    while True:
        print("1 - True")
        print("2 - False")
        
        puzzle_answer = input("Is this statement 'True': We will solve this together! (Yes or No)? Choose an option (1, 2): ")
        
        if puzzle_answer == "1":
            print("\nWell done!")
            break
        else:
            print("Wrong answer. Please try again.")

def bedroom1_return():
    """Return to Bedroom 1 after exploring Bedroom 2."""
    while True:
        print("\nWould you like to go back to Bedroom 1? (Yes or No)")
        action = input("Choose (Yes or No): ")
        if action.lower() == "yes":
            bedroom1()
        elif action.lower() == "no":
            break
        else:
            print("Invalid response. Please type 'Yes' or 'No'.")
