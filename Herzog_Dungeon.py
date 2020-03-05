import random
x_axis_coordinate = 2
y_axis_coordinate = 2
herzog_defeated = False
videotape_found = False
sadness_induced = False
key_found = False
exit_open = False


def herzog_random_quote():
  herzog_quotes = ["'I think there should be a holy war against yoga classes.'\n", "'The Universe is not harmonious; you know that by looking outside.'\n", "'The Universe is monstrously indifferent to the presence of Man.'\n", "'I\'m the last one who would do self-analysis.'\n","'I believe the common denominator of the universe is not harmony; but chaos, hostility and murder.'\n", "'I think psychology and self-reflection is one of the major catastrophes of the twentieth century.'\n", "'I prefer to be alive, so I\'m cautious about taking risks'\n", "'I'm not very eager to sit and look at my films all the time.'\n"]
  return random.choice(herzog_quotes)


def TV_selection():
  programmes = ["the newest episode of Weirder Stuff.", "a holy mass on Jesus TV.", "the newest episode of 'To catch a predator' with Chris Hansen.", "childish yet utterly creepy cartoons."]
  return random.choice(programmes)


def hall_room():
  print("This is the hall. Nothing here but four doors... That\'s weird.\n\n")  
  relocate_NESW()


def videotape_room():
  global videotape_found
  print("""This is a small room with only a TV cabinet and a weird, ancient-looking
device right under the TV set.\n\n""")
  choices = ["a","b","c"]  
  while True:
    answer = (input("""What do you do?:
Press A to watch some TV;
Press B to search the room;
Press C to exit the room:\n\n""")).lower()
    if answer not in choices:
      print("Sorry, wrong input.\n\n")
    elif answer == "a":
      print("You sit down and watch " + TV_selection()+" Some time has passed, you think it\'s time to go.\n\n")
    elif answer == "b":
      if videotape_found == False:
        videotape_found = True
        print("""You rummage through the debris, old TV guides, leftover food etc.
The only thing of interest you find is the weird, rectangular plastic box that appears to 
contain some sort of plastic tape. The writing on the box says 'The wild blue yonder'.
You put it in your inventory as it dawns on you thins might come in handy at some point.\n\n""")
      else:
        print("You find nothing of interest. Only broken dreams...\n\n")
    elif answer == "c":
      relocate_E()
      break


def sadness_room():
  global sadness_induced
  print("""This is a very dark, very sad room.
Nothing good can ever happen to you in here, you can only make yourself
sad by staying here...\n\n""")
  choices = ["a","b"]  
  while True:
    answer = (input("""What do you do?:
Press A to make yourself sad;
Press B to exit the room\n\n""")).lower()
    if answer not in choices:
      print("Sorry, wrong input.\n\n")
    elif answer == "a":
      if sadness_induced == False:
        sadness_induced = True
        print("""You ponder the inevitability of death and the ultimate
fruitlessness of all and any human activity. After a couple of hours
you feel so sad you consider becoming an emo edgelord even though
this trend ended many years ago fortunately.\n\n""")
      else:
        print("You\'re already bummed out and depressed, nothing more to gain, nothing to lose..\n\n")
    elif answer == "b":
      relocate_N()
      break


def key_room():
  global key_found
  print("""Ok, no bullshit, this is the key room, you can find the key here.\n\n""")
  choices = ["a","b"]  
  while True:
    answer = (input("""What do you do?:
Press A to grab the key;
Press B to exit the room.\n\n""")).lower()
    if answer not in choices:
      print("Sorry, wrong input.\n\n")
    elif answer == "a":
      if key_found == False:
        key_found = True
        print("""You find a weird-ass looking key. And it\'s covered in goo...\n\n""")
      else:
        print("You already got the key, get out.\n\n")
    elif answer == "b":
      relocate_W()
      break


def herzog_room():
  global herzog_defeated
  if herzog_defeated == False:
    input("""You enter a small, dark room. What little light the blinking, dilapidated
lamp casts on the surroundings is heavily obscured by a fog of cigarette fumes...\n\n""")
    input("""Then you begin to see it. At first just a silhouette - atrophied, slouching
as if constantly crushed by some ever-increasing sadness...\n\n""")
    input("""Your hear starts to race as you realize what that figure is...\n\n""")
    input("""A HERZOG! Adrenaline floods your system, your muscles flexed, your mind
wholly concentrated on the creature before you.\n\n""")
    choices = ["a","b","c","d"]
    while True:
      answer = (input("""What do you do?:
Press A to attack the HERZOG;
Press B to try and defeat HERZOG with your brain smarts
Press C to exit the room.\n\n""")).lower()
      if answer not in choices:
        print("Sorry, wrong input.\n\n")
      elif answer == "a":
        print("""You lunge at HERZOG flailing your arms wildly but he absorbs every punch
with a maddening calmness. After you\'ve exhausted your strength he looks away as if looking
at something very far away and utters:\n\n"""+herzog_random_quote())      
      elif answer == "b":
        if videotape_found == True and sadness_induced == True:
          herzog_defeated = True                
          print("""You sit down with HERZOG, light a cigarette and start a long and heartfelt
conversation about the nature of experience while watching his movie 'The wild blue yonder'. You both come to the conclusion that there is nothing holding you both in this virtual, fictional, half-baked and ridiculous universe and that it is high time this universe got terminated. HERZOG has been defeated and you can move onto the next room.\n\n""")
          break
        elif videotape_found == True:
          print("""You try to watch 'The wild blue yonder' with HERZOG but you give up 
after about six minutes as you are not nearly depressed enough to watch it.\n\n""")
        elif sadness_induced == True:
          print("""You would love to watch a movie and talk with HERZOG but you are unable to 
turn his attention away from spewing random quotes of himself. If only you had some item...\n\n""")
        else:
          print("""You posess neither the appropriate mindset nor the items necessary to defeat 
HERZOG. Come back when you do.\n\n""")
      else:
        relocate_S()
        break
  else:
    print("""The room is dark and shrouded with cigarette smoke but the HERZOG inside seems docile and only mutters quietly: \n\n"""+herzog_random_quote())    
    while True:
      answer = (input("""What do you do?:
Press A to exit the room;
""")).lower()
      if answer != "a":
        print("Sorry, wrong input.\n\n")
      else:
        relocate_NS()
        break


def exit_room():
  global key_found
  global exit_open
  print("This is the exit room. You can exit this nightmarish realm if you have the key...\n\n")  
  choices = ["a","b"]  
  while True:
    answer = (input("""What do you want to do?
Press A to end this nightmare and escape;
Press B to go back.\n\n""")).lower()
    if answer not in choices:
      print("Sorry, wrong input.\n\n")
    elif answer == "a":
      if key_found == True:
        exit_open = True
        print("""CONGRATULATIONS! You\'ve succesfully escaped the HERZOG dungeon!\n\n""")
        break
      else:
        print("The exit is locked.\n\n")
    elif answer == "b":
      relocate_S()
      break


def relocate_NESW():
  global y_axis_coordinate
  global x_axis_coordinate
  choices = ["n","s","w","e"]
  direction = (input("""Where do you want to go?
Press N to go north;
Press E to go east;
Press S to go south;
Press W to go west;\n\n""")).lower()
  while True:
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
      print("Sorry, wrong input.\n\n")


def relocate_NESW():
  global y_axis_coordinate
  global x_axis_coordinate
  choices = ["n","s","w","e"]
  direction = (input("""Where do you want to go?
Press N to go north;
Press E to go east;
Press S to go south;
Press W to go west;\n\n""")).lower()
  while True:
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
      print("Sorry, wrong input.\n\n")


def relocate_N():
  global y_axis_coordinate 
  direction = (input("""Where do you want to go?
Press N to go north;\n\n
""")).lower()
  while True:
    if direction == "n":
      y_axis_coordinate += 1
      break
    else:
      print("Sorry, wrong input.\n\n")
  

def relocate_S():
  global y_axis_coordinate
  direction = (input("""Where do you want to go?
Press S to go south;\n\n
""")).lower()
  while True:
    if direction == "s":
      y_axis_coordinate -= 1
      break
    else:
      print("Sorry, wrong input.\n\n")


def relocate_E():
  global x_axis_coordinate
  direction = (input("""Where do you want to go?
Press E to go east;\n\n
""")).lower()
  while True:
    if direction == "e":
      x_axis_coordinate += 1
      break
    else:
      print("Sorry, wrong input.\n\n")


def relocate_W():
  global x_axis_coordinate
  direction = (input("""Where do you want to go?
Press W to go west;\n\n
""")).lower()
  while True:
    if direction == "w":
      x_axis_coordinate -= 1
      break
    else:
      print("Sorry, wrong input.\n\n")


def relocate_NS():
  global y_axis_coordinate
  choices = ["n","s"]
  direction = (input("""Where do you want to go?
Press N to go north;
Press S to go south;
\n\n""")).lower()
  while True:
    if direction == "n":
      y_axis_coordinate += 1
      break
    elif direction == "s":
      y_axis_coordinate -= 1
      break   
    elif direction not in choices:
      print("Sorry, wrong input.\n\n")

def the_game():
  input("Welcome to the dungeon. Press ENTER to dive head-first into madness...")
  global exit_open
  while exit_open == False:
    if x_axis_coordinate == 2 and y_axis_coordinate == 2:
      hall_room()
    elif x_axis_coordinate == 2 and y_axis_coordinate == 1:
      sadness_room()
    elif x_axis_coordinate == 1 and y_axis_coordinate == 2:
      videotape_room()
    elif x_axis_coordinate == 3 and y_axis_coordinate == 2:
      key_room()
    elif x_axis_coordinate == 2 and y_axis_coordinate == 3:
      herzog_room()
    elif x_axis_coordinate == 2 and y_axis_coordinate == 4:
      exit_room()

  input("Press ENTER to quit.")

the_game()