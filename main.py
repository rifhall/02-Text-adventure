#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'ship.json'
item_file = 'items.json'


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


#tells you the name and desc for the current room
def render(game,items,current):
    c = game[current]
    print(c["name"])
    print(c["desc"])

    #displays items
    for i in c["items"]
        print(i["desc"])
    
#Where we get the players actions
def get_input():
    #asks for input
    print("What would you like to do?")
    #seperate for new line
    response = input()
    #make sure all exit(s) are one word and upper case
    response = response.upper().strip()
    return response

def update(game,items,current,response):
    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]
    return current


# The main function for the game
def main():
    current = 'DECK'  # The starting location
    end_game = ['END']  # Any of the end-game locations

    (game,items) = load_files()

    while True:
        render(game, items, current)
        response = get_input()
        
        #breaks the game if they type this 
        if response == "QUIT":
            break
        
        #will update the game
        current = update(game,items,current,response)


# run the main function
if __name__ == '__main__':
	main()