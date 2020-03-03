import requests
import random

def noun_or_adj():
  while True:
    selection = input("Enter A for an adjective or N for a noun: \n\n")     # input that will determine the keyword
    if selection == ("a").lower():                                           # for the API
      return "rel_jjb"             # per the API documentation this means 'select only adjectives'
      break
    elif selection == ("n").lower():
      return "rel_jja"             # per the API documentation this means 'select only nouns'
      break
    else:
      print("Sorry, wrong input. Please try again: \n\n")
      continue                     # safeguard for wrong input

def topic_select():                # input that will determine the keyword responsible for topic association
  while True:
    topicsel = (str(input("Enter a topic a word related to which you want to guess: \n"))).lower()
    if any(char.isdigit() for char in topicsel):    # safeguard against integers in input
      print("Sorry, wrong input.\n\n")
      continue
    elif len(topicsel.split()) > 1:                 # safeguard against multiple words in input
      print("Sorry, wrong input. Please limit answer to a single word.\n\n")
    else:
      return str(topicsel)

def secret_word_selection():
  parameter = {noun_or_adj():topic_select(), "max":100}              # creating the full parameter for the api end point
  req = (requests.get("http://api.datamuse.com/words",parameter)).json()      #reaching data in end point
  words = []
  for w in req:                                                               # creating an array of possible words
    words.append(w["word"])                                                   # that meet the key criteria
  secretword = random.choice(words)                                           # selecting one of those words
  return str(secretword)

secretword = secret_word_selection()

print("The secret word has " + str(len(secretword)) + " letters. \n\n")     # a clue for the player

def guessword():
  global secretword

  # defining variables:

  counter = 0                           # counter to help control the number of iterations
  max_counter = len(secretword)         # the limit of iterations based on counter
  guesses = list(len(secretword)*"_")   # create a list - empty at first will be populated with guessed letters

  # commencing loop:
  while True:

    ans = input("""Enter your quess (letter or word)
or enter '0' if you\'re a little quitter bitch: \n\n""")  # user input
    if ans == "0":
      print("The secret word was: " + secretword)
      break
    elif len(ans) > 1:                                  # safeguard against partial word input since we want the user
      if ans == secretword:                             # to input either a single char or the entire word
        print(secretword)
        print("You win.\n")
        break
      else:
        print("Nope, that\'s not it.\n")
        counter += 1
    elif ans in secretword:                             # if answer char is indeed a part of the secret word
      for n in range(len(secretword)):                  # a quick loop to determine the index at which the char is
        if ans == secretword[n]:                        # located in the secret word and to put it at analogous
          guesses[n] = str(ans)                         # index in quesses: we want to show the player their
          print("Yes! You got one. \n")                 # partial answer
          partial = "".join([x for x in guesses])       # turning list into string for printing of partial answer
          print(partial)
    else:
      counter += 1                                      # if answer is neither the secret word nor a part of it
      print("Nope, try again. \n")                      # counter + 1 and message
      partial = "".join([x for x in guesses])           # turning list into string for printing of partial answer
      print(partial)
    if counter >= max_counter:                          # loop termination if counter reaches limit
      print("No more tries. Better luck next time.\n")
      break

guessword()

input("Press ENTER to quit.")



