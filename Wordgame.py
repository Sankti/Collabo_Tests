import random
import difflib

wordlist = open('words.txt', 'r')
words = [line[:-1] for line in wordlist]
wordlist.close()

print(words)

def select_secret_word():
  secret = random.choice(words)
  return secret

""" 
the above function should always
return a random value from our 
list of words stored in file
"""

def find_rhyme(x):
  rhyme = str(difflib.get_close_matches(x,[words],1))
  return rhyme

"""
the above function will return 
from the word list a word similar
to the x
"""

print("Guess what word I am thinking about.\n")
while True:
  select_secret_word()
  sel = str.lower(input("""You can ask me questions about the word:\n
Press A to see what words the word rhymes with,
press B to see how long the word is,
or type in the word if you think you've guessed it:\n"""))

  if sel == "a":
    print("The word rhymes with " + (find_rhyme(select_secret_word())) + "\n")
  elif sel == "b":
    print("The word is " + str(len(select_secret_word())) + " letters long. \n")
  elif sel == select_secret_word():
    break
    print("Yes! The answer is: " + str(select_secret_word)
    + ". Well done!\n")

input("Press ENTER to quit.")