print("HANGMAN ver 1.2 \n")
print("This is a very simple hangman program based on loops.\n")
print("""Every time you are asked for input enter a letter that you think 
the answer contains or the full word if you think you guessed it.

You can use both capital and regular letters!\n""")

beverage = ["_","_","_","_"]
hangman = ("""\n-----------\n|         |\n|          \n|          \n|          \n|          \n|\n|\n|\n""")
counter = 0
print(beverage)
print(hangman)

while beverage != ["B","E","E","R"] and counter < 4:
  ans = input("Enter a letter or a word:")
  if ans == "R" or ans == "r":
    beverage[3] = "R"
    print(beverage)
    print(hangman)
    
  elif ans == "B" or ans == "b":
    beverage[0] = "B"
    print(beverage)
    print(hangman)
    
  elif ans == "E" or ans == "e":
    beverage[1] = "E"
    beverage[2] = "E"
    print(beverage)
    print(hangman)

  elif ans == "BEER" or ans == "beer" or ans == "Beer":
    beverage = ["B","E","E","R"]

  else:
    counter = counter + 1
    if counter == 1:
      print(beverage)
      hangman = ("""\n-----------\n|         |\n|         O\n|            \n|            \n|          \n|\n|\n|\n""")
      print(hangman)
      print("Wrong, dummy!!!\n")
    elif counter == 2:
      print(beverage)
      hangman = ("""\n-----------\n|         |\n|         O\n|        /|\ \n|            \n|          \n|\n|\n|\n""")
      print(hangman)
      print("Wrong, dummy!!!\n")
    elif counter == 3:
      print(beverage)
      hangman = ("""\n-----------\n|         |\n|         O\n|        /|\ \n|        /   \n|          \n|\n|\n|\n""")
      print(hangman)
      print("Wrong, dummy!!!\n")
    
if beverage == ["B","E","E","R"]:
  print(beverage)
  print(hangman)
  print("Whooptie doo, you got it. You\'re probably an alcoholic.\n")
   
if counter == 4:
  print("""\n-----------\n|         |\n|         O\n|        /|\ \n|        / \ \n|          \n|\n|\n|\n""")
  print("Sorry, you've lost. There is no hope for you, ever. Better drop everything and go live in the woods..\n")
  
input("Press enter to exit HANGMAN: ")