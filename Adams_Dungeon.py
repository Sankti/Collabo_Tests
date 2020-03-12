location = 32    # Starting location

dungeon_map = [
    10, 11, 12, 13, 14,
    20, 21, 22, 23, 24,
    30, 31, 32, 33, 34
]

dungeon_locations = {
    11 : "Alchemyst's Domain",
    13 : "Hall of the Wicked",
    14 : "Sage's Cell",
    21 : "Corridor of Snakes",
    22 : "Entrance Hall",
    23 : "Corridor of Traps",
    24 : "Death Room",
    32 : "Dungeon Gate",
}

def room(number):
    print("\n   °º¤ø,¸¸,ø¤º°   ")
    print("You are now in " + dungeon_locations[number] + ".")
    change_location()

def change_location():
    global location

    while True:
        print("Please select your destination:")
        destination = input("[n]orth, [w]est, [e]ast or [s]outh: ").lower()

        if destination not in ("n", "w", "e", "s"):
            print("Invalid direction. Please try again.")

        elif destination == "n":
            location -= 10
            if check_validity(location) == False:
                location += 10
                print("\nA solid wall is blocking the way.")
            else:
                break

        elif destination == "w":
            location -= 1
            if check_validity(location) == False:
                location += 1
                print("\nA solid wall is blocking the way.")
            else:
                break

        elif destination == "e":
            location += 1
            if check_validity(location) == False:
                location -= 1
                print("\nA solid wall is blocking the way.")
            else:
                break

        elif destination == "s":
            location += 10
            if check_validity(location) == False:
                location -= 10
                print("\nA solid wall is blocking the way.")
            else:
                break
            
    room(location)

def check_validity(coords):
    if coords not in dungeon_locations.keys():
        return False
    else:
        return True

def play(coords):
    print("Welcome, Adventurer.")
    room(coords)
    change_location()

play(location)
