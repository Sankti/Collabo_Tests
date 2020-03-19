player = {
    "attributes": {},
    "skills": {}
}

attribs = {
    "starsign": {
        1: "Liberace",
        2: "The constellation formerly known as Prince",
        3: "Vomitus"
    },
    "provenience": {
        1: "multi-generation village idiot",
        2: "stuck-up noble",
        3: "a mage that\'s slightly inappropriate with male apprentices"
    }
}

da_list = ["stamina", "tomfoolery", "charisma", "strength"]


def wrong_input():
    print("Sorry, wrong input, try again.\n")


def attributes_setup(attributes_dict):
    global player
    for attribute in attributes_dict:
        attribute_selected = None
        while attribute_selected is None:
            print("Select your character's " + attribute + ".\nThe available choices are:\n """)
            for key in attributes_dict[attribute]:
                print("Press " + str(key) + " for " + attributes_dict[attribute][key])
            try:
                answer = (int(input(":\n")))
                if answer in attributes_dict[attribute]:
                    attribute_selected = attributes_dict[attribute][answer]
                else:
                    wrong_input()
            except ValueError:
                wrong_input()
        player["attributes"][attribute] = attribute_selected


def set_up_single_skill(total_points, skill_min, skill_max, skill_list):
    global player
    total = total_points
    for s in skill_list:
        skill_value = None
        while skill_value not in range(skill_min, skill_max + 1):
            try:
                if s == skill_list[-1]:
                    skill_value = total
                    break
                answer = int(input("How many for: " + s + "?\n"))
                if 0 < answer <= skill_max:
                    if s != skill_list[-2] and answer <= total:
                        total -= answer
                        skill_value = answer
                    elif s == skill_list[-2] and answer == total:
                        print("Sorry, can\'t do that, you got " + str(total) + " points left and two skills left.\n")
                        continue
                    elif s == skill_list[-2] and answer < total:
                        total -= answer
                        skill_value = answer
                    elif s == skill_list[-1]:
                        skill_value = total
                    else:
                        print("Not enough points. You got " + str(total) + " left to assign.\n")
                        continue
                else:
                    print("Please enter a number between " + str(skill_min) + " and " + str(skill_max) + ".\n")
            except ValueError:
                wrong_input()
        player["skills"][s] = skill_value


def skills_setup(total_points, skill_min, skill_max, skill_list):
    global player
    print("\nMinimum of " + str(skill_min) + " and Maximum of " + str(skill_max) + " can be devoted to a skill.\n")
    set_up_single_skill(total_points, skill_min, skill_max, skill_list)


def full_character_setup():
    skills_setup(12, 1, 5, da_list)
    attributes_setup(attribs)
    print(player)

full_character_setup()





