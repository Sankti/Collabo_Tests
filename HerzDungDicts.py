import random

herzog_quotes = {
    1: "'I think there should be a holy war against yoga classes.'\n",
    2: "'The Universe is not harmonious; you know that by looking outside.'\n",
    3: "'The Universe is monstrously indifferent to the presence of Man.'\n",
    4: "'I\'m the last one who would do self-analysis.'\n",
    5: "'I believe the common denominator of the universe is not harmony; but chaos, hostility and murder.'\n",
    6: "'I think psychology and self-reflection is one of the major catastrophes of the twentieth century.'\n",
    7: "'I prefer to be alive, so I\'m cautious about taking risks'\n",
    8: "'I'm not very eager to sit and look at my films all the time.'\n"
}

tv_programmes = {
    1: "the newest episode of Weirder Stuff.\n",
    2: "a holy mass on Jesus TV.\n",
    3: "the newest episode of 'To catch a predator' with Chris Hansen.\n",
    4: "a cooking show with a very old an unattractive host.\n",
    5: "a WW2 documentary with a slightly anti-semitic angle.\n"
}

rooms = {
    "videotape_room": {
        "intro": """This is a small room with only a TV cabinet and a weird, ancient-looking
device right under the TV set.\n\n""",
        "input_message": """What do you do?:
Press A to watch some TV;
Press B to search the room;
Press C to exit the room:\n\n""",
        "choices": ["a", "b", "c"],
        "action_messages": {
            "watching_tv": "You sit down for a couple minutes and watch ",
            "first_search": """You rummage through the debris, old TV guides, leftover food etc.
The only thing of interest you find is the weird, rectangular plastic box that appears to 
contain some sort of plastic tape. The writing on the box says 'The wild blue yonder'.
You put it in your inventory as it dawns on you thins might come in handy at some point.\n\n""",
            "further_searches": "You find nothing of interest. Only broken dreams...\n\n"
        }},
    "sadness_room": {
        "intro": """This is a very dark, very sad room. 
Nothing good can ever happen to you in here, you can only make yourself
sad by staying here...\n\n""",
        "input_message": """What do you do?:
Press A to make yourself sad;
Press B to exit the room\n\n""",
        "choices": ["a", "b"],
        "action_messages": {
            "first_sadness": """You ponder the inevitability of death and the ultimate
fruitlessness of all and any human activity. After a couple of hours
you feel so sad you consider becoming an emo edgelord even though
this trend ended many years ago fortunately.\n\n""",
            "further_sadness": "You\'re already bummed out and depressed, nothing more to gain, nothing to lose..\n\n"
        }},
    "key_room": {
        "intro": "Ok, no bullshit, this is the key room, you can find the key here.\n\n",
        "input_message": """What do you do?:
Press A to grab the key;
Press B to exit the room.\n\n""",
        "choices": ["a", "b"],
        "action_messages": {
            "first_key_search": "You find a weird-ass looking key. And it\'s covered in goo...\n\n",
            "further_key_search": "You already got the key, get out.\n\n"
        }},
    "herzog_room": {
        "intro_pre_defeat1": """You enter a small, dark room. What little light the blinking, dilapidated
lamp casts on the surroundings is heavily obscured by a fog of cigarette fumes...\n\n""",
        "intro_pre_defeat2": """Then you begin to see it. At first just a silhouette - atrophied, slouching
as if constantly crushed by some ever-increasing sadness...\n\n""",
        "intro_pre_defeat3": """Your hear starts to race as you realize what that figure is...\n\n""",
        "intro_pre_defeat4": """A HERZOG! Adrenaline floods your system, your muscles flexed, your mind
wholly concentrated on the creature before you.\n\n""",
        "intro_post_defeat": """The room is dark and shrouded with cigarette smoke but the HERZOG seems docile 
and only mutters quietly: \n\n""" + random.choice(list(herzog_quotes.values())),
        "input_message_pre_defeat": """What do you do?:
Press A to attack the HERZOG;
Press B to try and defeat HERZOG with your brain smarts
Press C to exit the room.\n\n""",
        "input_message_post_defeat": """What do you do?:
Press A to exit the room;""",
        "choices": ["a", "b", "c"],
        "action_messages": {
            "attack": """You lunge at HERZOG flailing your arms wildly but he absorbs every punch
with a maddening calmness. After you\'ve exhausted your strength he looks away as if looking
at something very far away and utters:\n\n""" + random.choice(list(herzog_quotes.values())),
            "smart_defeat": """You sit down with HERZOG, light a cigarette and start a long and heartfelt
conversation about the nature of experience while watching his movie 'The wild blue yonder'. 
You both come to the conclusion that there is nothing holding you both in this virtual, fictional, half-baked 
and ridiculous universe and that it is high time this universe got terminated. HERZOG has been defeated 
and you can move onto the next room. """,
            "videotape_only": """You try to watch 'The wild blue yonder' with HERZOG but you give up 
after about six minutes as you are not nearly depressed enough to watch it.\n\n""",
            "sadness_only": """You would love to watch a movie and talk with HERZOG but you are unable to 
turn his attention away from spewing random quotes of himself. If only you had some item...\n\n""",
            "unprepared": """You posess neither the appropriate mindset nor the items necessary to defeat 
HERZOG. Come back when you do.\n\n"""
        }},
    "exit_room": {
        "intro": "This is the exit room. You can exit this nightmarish realm if you have the key...\n\n",
        "input_message": """What do you want to do?
Press A to end this nightmare and escape;
Press B to go back.\n\n""",
        "choices": ["a", "b"],
        "action_messages": {
            "key_found": "CONGRATULATIONS! You\'ve succesfully escaped the HERZOG dungeon!\n\n",
            "key_not_found": "The exit is locked.\n\n"
        }}}
