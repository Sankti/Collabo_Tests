import random

secret = "x"

wordlist = open('words.txt', 'r')
words = [line[:-1] for line in wordlist]
wordlist.close()

def create_suffix(x):
  suffix = str(str(x[int(len(x)-4)]) + str(x[int(len(x)-3)]) 
  + str(x[int(len(x)-2)]) + str(x[int(len(x)-1)]))
  return suffix

def create_suffix2(x):
  suffix2 = str(str(x[int(len(x)-4)]) + str(x[int(len(x)-3)]) 
  + str(x[int(len(x)-2)]) + str(x[int(len(x)-1)]))
  return suffix2

"""
the above function will create a suffix of 
a word by putting together it's four last
letters
"""

def select_secret_word():
  global secret
  secret = random.choice(words)
  return secret

def find_rhyme(x):
  while True:
    possible_rhyme = random.choice(words)
    if str(create_suffix(possible_rhyme)) == str(create_suffix2(secret)):
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

select_secret_word()

while True:
  
  sel = str.lower(input("""You can ask me questions about the word:\n
Press A to see what words the word rhymes with,
press B to see how long the word is,
or type in the word if you think you've guessed it:\n"""))
  
  if sel == "a":
    print("The word rhymes with " + (find_rhyme(secret)) + "\n")
  elif sel == "b":
    print("The word is " + str(len(secret)) + " letters long. \n")
  elif sel == select_secret_word():
    print("Yes! The answer is: " + str(secret) + ". Well done!\n")
    break

input("Press ENTER to quit.")