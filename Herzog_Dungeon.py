import random
import HerzDungDicts

all_possible_coordinates = [(2, 2), (2, 1), (1, 2), (3, 2), (2, 3)]
x_axis_coordinate = 2
y_axis_coordinate = 2
current_position = (x_axis_coordinate, y_axis_coordinate)
herzog_defeated = False
videotape_found = False
sadness_induced = False
key_found = False
exit_open = False
incorrect_inp = "Sorry, wrong input.\n\n"


def hall_room():
    print("This is the hall. Nothing here but four doors... That\'s weird.\n\n")
    relocate()


def videotape_room():
    global videotape_found
    global incorrect_inp
    print(HerzDungDicts.rooms["videotape_room"]["intro"])
    choices = HerzDungDicts.rooms["videotape_room"]["choices"]
    while True:
        answer = (input(HerzDungDicts.rooms["videotape_room"]["input_message"])).lower()
        if answer not in choices:
            print(incorrect_inp)
        elif answer == "a":
            print(HerzDungDicts.rooms["videotape_room"]["action_messages"]["watching_tv"] +
                  random.choice(list(HerzDungDicts.tv_programmes.values())))
        elif answer == "b":
            if videotape_found is False:
                videotape_found = True
                print(HerzDungDicts.rooms["videotape_room"]["action_messages"]["first_search"])
            else:
                print(HerzDungDicts.rooms["videotape_room"]["action_messages"]["further_searches"])
        elif answer == "c":
            relocate()
            break


def sadness_room():
    global sadness_induced
    global incorrect_inp
    print(HerzDungDicts.rooms["sadness_room"]["intro"])
    choices = HerzDungDicts.rooms["sadness_room"]["choices"]
    while True:
        answer = (input(HerzDungDicts.rooms["sadness_room"]["input_message"])).lower()
        if answer not in choices:
            print(incorrect_inp)
        elif answer == "a":
            if sadness_induced is False:
                sadness_induced = True
                print(HerzDungDicts.rooms["sadness_room"]["action_messages"]["first_sadness"])
            else:
                print(HerzDungDicts.rooms["sadness_room"]["action_messages"]["further_sadness"])
        elif answer == "b":
            relocate()
            break


def key_room():
    global key_found
    global incorrect_inp
    print(HerzDungDicts.rooms["key_room"]["intro"])
    choices = HerzDungDicts.rooms["key_room"]["choices"]
    while True:
        answer = (input(HerzDungDicts.rooms["key_room"]["input_message"])).lower()
        if answer not in choices:
            print(incorrect_inp)
        elif answer == "a":
            if key_found is False:
                key_found = True
                print(HerzDungDicts.rooms["key_room"]["action_messages"]["first_key_search"])
            else:
                print(HerzDungDicts.rooms["key_room"]["action_messages"]["further_key_search"])
        elif answer == "b":
            relocate()
            break


def herzog_room():
    global herzog_defeated
    global all_possible_coordinates
    global incorrect_inp
    if herzog_defeated is False:
        input(HerzDungDicts.rooms["herzog_room"]["intro_pre_defeat1"])
        input(HerzDungDicts.rooms["herzog_room"]["intro_pre_defeat2"])
        input(HerzDungDicts.rooms["herzog_room"]["intro_pre_defeat3"])
        input(HerzDungDicts.rooms["herzog_room"]["intro_pre_defeat4"])
        choices = HerzDungDicts.rooms["herzog_room"]["choices"]
        while True:
            answer = (input(HerzDungDicts.rooms["herzog_room"]["input_message_pre_defeat"])).lower()
            if answer not in choices:
                print(incorrect_inp)
            elif answer == "a":
                print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["attack"])
            elif answer == "b":
                if videotape_found is True and sadness_induced is True:
                    all_possible_coordinates.append((2, 4))
                    herzog_defeated = True
                    print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["smart_defeat"])
                    break
                elif videotape_found is True:
                    print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["videotape_only"])
                elif sadness_induced is True:
                    print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["sadness_only"])
                else:
                    print(HerzDungDicts.rooms["herzog_room"]["action_messages"]["unprepared"])
            else:
                relocate()
                break
    else:
        print(HerzDungDicts.rooms["herzog_room"]["intro_post_defeat"])
        while True:
            answer = (input(HerzDungDicts.rooms["herzog_room"]["input_message_post_defeat"])).lower()
            if answer != "a":
                print(incorrect_inp)
            else:
                relocate()
                break


def exit_room():
    global key_found
    global exit_open
    global incorrect_inp
    print(HerzDungDicts.rooms["exit_room"]["intro"])
    choices = HerzDungDicts.rooms["exit_room"]["choices"]
    while True:
        answer = (input(HerzDungDicts.rooms["exit_room"]["input_message"])).lower()
        if answer not in choices:
            print(incorrect_inp)
        elif answer == "a":
            if key_found is True:
                exit_open = True
                print(HerzDungDicts.rooms["exit_room"]["action_messages"]["key_found"])
                break
            else:
                print(HerzDungDicts.rooms["exit_room"]["action_messages"]["key_not_found"])
        elif answer == "b":
            relocate()
            break


def relocate():
    global y_axis_coordinate
    global x_axis_coordinate
    global incorrect_inp
    choices = []
    if (x_axis_coordinate + 1, y_axis_coordinate) in all_possible_coordinates:
        choices.append("e")
        print("Press 'E' to go east;")
    if (x_axis_coordinate - 1, y_axis_coordinate) in all_possible_coordinates:
        choices.append("w")
        print("Press 'W' to go west;")
    if (x_axis_coordinate, y_axis_coordinate + 1) in all_possible_coordinates:
        choices.append("n")
        print("Press 'N' to go north;")
    if (x_axis_coordinate, y_axis_coordinate - 1) in all_possible_coordinates:
        choices.append("s")
        print("Press 'S' to go south;")
    while True:
        direction = (input("Select direction:\n")).lower()
        if direction == "n":
            y_axis_coordinate += 1
            break
        elif direction == "e":
            x_axis_coordinate += 1
            break
        elif direction == "s":
            y_axis_coordinate -= 1
            break
        elif direction == "w":
            x_axis_coordinate -= 1
            break
        elif direction not in choices:
            print(incorrect_inp)


def the_game():
    input("Welcome to the dungeon. Press ENTER to dive head-first into madness...")
    global exit_open
    while exit_open is False:
        current_position = (x_axis_coordinate, y_axis_coordinate)
        if current_position == (2, 2):
            hall_room()
        elif current_position == (2, 1):
            sadness_room()
        elif current_position == (1, 2):
            videotape_room()
        elif current_position == (3, 2):
            key_room()
        elif current_position == (2, 3):
            herzog_room()
        elif current_position == (2, 4):
            exit_room()
    input("Press ENTER to quit.")


the_game()
