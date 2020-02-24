from random import choice
from string import capwords

# Setting the <<points>> variable:

points = 0

# Defining <<States : Capitals>> dictionary:

capitals = {
  "California" : "Sacramento",
  "Maine" : "Augusta",
  "Nebraska" : "Lincoln",
  "New York" : "Albany",
  "Wyoming" : "Cheyenne",
  "Massachusetts" : "Boston",
  "Delaware" : "Dover",
  "Ohio" : "Columbus",
  "New Mexico" : "Santa Fe"
  }

# Defining game mechanics functions:

def choose_question():
  """
  Returns string:  a random KEY
  from dictionary capitals.
  """
  return choice(list(capitals.keys()))

def ask_question(capital):
  """
  Asks user for input: changes
  int score based on validity
  of the user's answer. Answer
  must be string equal to VALUE
  of capital KEY in capitals dict.
  """
  global points
  answer = capwords(input("What is the capital of "
                 + capital +"?\n\n"))
  if answer == capitals[capital]:
    points += 100
    print("Correct. You receive a 100 points!\n")
  else:
    points -= 100
    print ("Ooo, sorry, that\'s not correct dumbo. "
           + "You lose a 100 points! \n")

def final_score():
  """
  Prints final valuation based
  on user's score.
  """
  if points == 100:
    print("That's all the questions. You got:\n"
          + str(points) + " points. Meh, I\'ve seen better.\n\n")
  elif points == 200:
    print("That's all the questions. You got:\n" + str(points)
          + " points. Try harder next time.\n\n")
  elif points == 300:
    print("That's all the questions. You got:\n" + str(points)
          + " points. Good, you passed Einstein.\n\n")
  elif points <= 0:
    print("That's all the questions. You got:\n" + str(points)
          + " points. You are retarded.\n\n")

def game():
  """
  Commences the game: asks user
  three questions and then
  evaluates their final score.
  """
  input("Welcome to the United States Capitals Quiz v 1.0. "
        + "KING ADAM mod v. 0.69 "
        + "Press Enter to continue.\n\n")
  input("You will be presented with three questions regarding "
        + "USA State Capitals.\nYou will receive a 100 points "
        + "for each correct answer\nand lose a 100 points for "
        + "each wrong answer. Press ENTER when you\'re ready "
        + "for your first question.")
  for number in range(3):
    ask_question(choose_question())
  final_score()
  input("Press ENTER to quit.")

# Commencing the game:

game()
