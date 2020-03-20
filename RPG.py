player = {}

attribs = {
    "Starsign": {
        1: "Liberace",
        2: "The constellation formerly known as Prince",
        3: "Vomitus"
    },
    "Provenience": {
        1: "multi-generation village idiot",
        2: "stuck-up noble",
        3: "a mage that\'s slightly inappropriate with male apprentices"
    }
}


da_list = ["Stamina", "Tomfoolery", "Swagger", "Strength", "Brainsmarts", "Liver-power", "Witicism"]


def wrong_input():
    input("\nSorry, wrong input, press ENTER to try again.\n")


def attributes_setup(attributes_dict, attributes_list_name):
    global player
    player[attributes_list_name] = {}
    for attribute in attributes_dict:
        attribute_selected = None
        while attribute_selected is None:
            print("\nSelect your character's " + attribute + ".\n")
            for key in attributes_dict[attribute]:
                print("Press " + str(key) + " for " + attributes_dict[attribute][key])
            try:
                answer = (int(input("")))
                if answer in attributes_dict[attribute]:
                    attribute_selected = attributes_dict[attribute][answer]
                else:
                    wrong_input()
            except ValueError:
                wrong_input()
        player[attributes_list_name][attribute] = attribute_selected


def set_up_single_skill(total_points, skill_min, skill_max, skill_list, skillset_name):
    global player
    total = total_points - (len(skill_list) * skill_min)
    player[skillset_name] = {}  
    for s in skill_list:
        player[skillset_name][s] = skill_min
    for s in skill_list:
        skill_value = 0
        while True:            
            try:
                print("You got " + str(total) + " points left.")
                answer = int(input("\nAssign points to " + str(s) + ".\n"))
                if answer <= total:                    
                    if 0 <= answer <= (skill_max - skill_min):
                        skill_value += answer
                        total -= answer
                        break
                    else:
                        print("\nPlease select value between 0 and " + str(skill_max - skill_min) + ".\n")
                        continue
                else:
                    print("\nNot enough points. You got " + str(total) + " points.\n")                    
            except ValueError:
                wrong_input
                continue                
        player[skillset_name][s] += skill_value
    if total > 0:
      print("\nYou have unused points!!!\n")
 

def skills_setup(total_points, skill_min, skill_max, skill_list, skillset_name):
    input("\nMinimum of 0 and a maximum of " + str(skill_max - 1) + " can be devoted to a skill. Press ENTER.\n")
    set_up_single_skill(total_points, skill_min, skill_max, skill_list, skillset_name)


def set_up_review(player_dict_segment):
    while True:
        for key in player_dict_segment:
            print(key + " : " + str(player_dict_segment[key]))
        answer = (input("\nPress Y to proceed and N to re-set.\n")).lower()
        if answer == "y":
            ready = True
            break
        elif answer == "n":
            ready = False
            break
        else:
            wrong_input()
            continue
    return ready
   

def full_character_setup():
    ready = False
    while ready is False:
        skills_setup(23, 1, 5, da_list, "Umiejetnosci")
        ready = set_up_review(player["Umiejetnosci"])
    ready = False     
    while ready is False:
        attributes_setup(attribs, "Atrybuty")
        ready = set_up_review(player["Atrybuty"])        
    print(player)


full_character_setup()


    
    
    
    
