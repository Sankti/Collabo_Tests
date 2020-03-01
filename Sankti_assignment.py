s = "abbbbbbbbbdwiiiiiii"

current_index = 0                     # starting position 
current_letter = s[current_index]     # current letter
next_letter = s[current_index + 1]    # next letter in string relative to current
string = ""                           # starting string    
temp = current_letter                 # temporary letter cache

for char in s:  

# step 1 - verify whether next letter > than current letter:

  if next_letter >= char:
    temp = temp + next_letter   # if yes: cache has next letter added  
  else:
    temp = next_letter          # if not: cache 'switches' to next letter

# step 2 - update index:
  current_index += 1        

#step 3 - safeguard against error (index out of range) when we near the end of 's':
  if current_index < len(s) - 1:      # if yes: proceed normally
    next_letter = s[current_index + 1]
  else:                               
    # if no and current index IS the second to last letter: consider last letter empty
    next_letter = ""

#step 4 - safeguard against error if s consists of unique chars and their values are 
# ordered backwards - i.e. reversed alphabet:
  if string == "":
    string = char

#step 5 - verify whether the length of cache exceeds the length of string:
  if len(temp)>len(string):           #if yes: substitute string with cache
    string = temp

print(string)
  


