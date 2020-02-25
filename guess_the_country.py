from random import choice

poland = {
  "population": "about 38m",
  "continent": "Europe",
  "colours": "red and white",
  "ethnicity": "slavic",
  "name": "Poland"

}

germany = {
  "population": "about 80m",
  "continent": "Europe",
  "colours": "black, red and yellow",
  "ethnicity": "germanic",
  "name": "Germany"
}

france = {
  "population": "about 67m",
  "continent": "Europe",
  "colours": "blue, white and red",
  "ethnicity": "franconic",
  "name": "France"
}

china = {
  "population": "about 1.5b",
  "continent": "Asia",
  "colours": "red and yellow",
  "ethnicity": "han",
  "name": "China"
}

argentina = {
  "population": "about 44m",
  "continent": "South America",
  "colours": "blue and white",
  "ethnicity": "mixed hispanic and native south american",
  "name": "Argentina"
}

countries = [poland, germany, france, china, argentina]

def secretCountry():
  return choice(countries)

answer = secretCountry()
print("""I\'m thinking of a country, can you guess what country it is?\n
Enter A to find out population,
enter B to find out what continen the country lies on,
enter C to find out what the national colours are,
enter D to find out the general ethnicity of the population,
enter Q to quit and display answer
or type in the name of the country if you\'ve guessed it:\n""")

while True:
  ans = (str(input(":"))).lower()
  if ans == "a":
    print("The population is " + answer["population"] + ".\n")
  elif ans == "b":
    print("The continent is " + answer["continent"] + ".\n")    
  elif ans == "c":
    print("The colours are " + answer["colours"] + ".\n")    
  elif ans == "d":
    print("The ethnicity is " + answer["ethnicity"] + ".\n")    
  elif ans == "q":
    print("The name is " + answer["name"] + ".\n")
    break
  elif ans == (answer["name"]).lower():
    print("Yes! The country is " + answer["name"] + ". You win!\n")
    break
  else:
    print("Sorry, that\'s not it. Try again.")
  
input("Press ENTER to quit:\n")