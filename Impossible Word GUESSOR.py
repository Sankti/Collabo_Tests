import random
from time import sleep

wordlist = open('words.txt', 'r')
words = [line[:-1] for line in wordlist]
wordlist.close()

def create_suffix(x):
  suffix = str(str(x[int(len(x)-4)]) + str(x[int(len(x)-3)]) 
  + str(x[int(len(x)-2)]) + str(x[int(len(x)-1)]))
  return suffix

"""
the above function will create a suffix of 
a word by putting together it's four last
letters
"""

def select_secret_word():
  return random.choice(words)

secret = select_secret_word()

def find_rhyme(x):
  while True:
    possible_rhyme = random.choice(words)
    if str(create_suffix(possible_rhyme)) == str(create_suffix(x)):
      break
    else:
      continue

  return possible_rhyme  

""" 
the above function find_rhyme should always
return a random value from our 
list of words stored in file
"""

print("Guess what word I am thinking about.\n")

# GUESSOR

def g_GUESSOR():
  print("       .---.\n      /_____\   I am Guessor.\n      ( '.' )   Let me handle this.\n       \_-_/_\n    .-'`'V'//-.")
  sleep(2)
  guess = ""
  counter = 0
  base_rhyme = find_rhyme(secret)
  print("You're saying that your word is " + str(len(secret)) + " letters long and rhymes with " + base_rhyme + "...")
  while guess != secret:
    counter += 1
    guess = find_rhyme(base_rhyme)
    print("Guess no. " + str(counter) + ": " + guess + "!")
  print("I got your word! It is " + guess + "!")
  if counter == 1:
    print("It took me " + str(counter) + " guess to figure it out!\n")
  else:
    print("It took me " + str(counter) + " guesses to figure it out!\n")

# END GUESSOR

while True:
  
  sel = str.lower(input("""You can ask me questions about the word:\n
Press A to see what words the word rhymes with,
press B to see how long the word is,
or type in the word if you think you've guessed it:\n"""))
  
  if sel == "a":
    print("The word rhymes with " + (find_rhyme(secret)) + "\n")
  elif sel == "b":
    print("The word is " + str(len(secret)) + " letters long. \n")
  elif sel == secret:
    print("Yes! The answer is: " + str(secret) + ". Well done!\n")
    break
  elif sel == "guessor":
    g_GUESSOR()

input("Press ENTER to quit.")
