#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'ship.json'
item_file = 'items.json'

#setting up variables
inventory = []
moves = 0


# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        with open(os.path.join(__location__, item_file)) as json_file: items = json.load(json_file)
        return (game,items)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)

#only displays an item only if it is not in your inventory
def check_inventory(item):
    for i in inventory:
        if i == item:
            return True
    return False


#tells you the name and desc for the current room
def render(game,items,current,moves):
    c = game[current]
    print("\n",c["name"])
    print(c["desc"])
    
#Where we get the players actions
def get_input():
    #asks for input
    print("\nWhat would you like to do?")
    #seperate for new line
    response = input()
    #make sure all exit(s) are one word and upper case
    response = response.upper().strip()
    return response

def update(game,items,current,response):
    #allows the player to check their inventory
    if response == "INVENTORY":
        print("You are carrying:")
        if len(inventory) == 0:
            print("Nothing")
        else:
            for i in inventory:
                print(i.lower())
        return current

    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]
    
    #will go through all the available items if they type get
    if response == "GET":
        #does a for loop for all items
        for i in c["items"]:
            #prints all the items
            print(i["item"])
            which = input()
            which = which.upper()
            if (which == i["item"]) and not (check_inventory(i["item"])):
                print(i["take"])
                inventory.append(i["item"])
        return current

    return current


# The main function for the game
def main():
    current = 'BEGIN'  # The starting location
    end_game = ['END']  # Any of the end-game locations
    moves = 0 #moves the player has taken

    (game,items) = load_files()

    while True:
        render(game, items, current, moves)
        response = get_input()
        
        #breaks the game if they type this 
        if response == "QUIT":
            break
        
        #will update the game
        current = update(game,items,current,response)
        moves += 1 #updates moves
    
    print("\nThank you for playing")
    print("You took {} moves".format(moves))


# run the main function
if __name__ == '__main__':
	main()