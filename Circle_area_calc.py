def circle_area(x):
  pi = 3.141592
  area = pi * (float(x)*float(x))
  print("The area of a wheel with a radius of " + x + "cm is " + (str(round(float(area),4)) + "cm2.\n"))

while True:
  r = input("""Enter radius value in cm
or enter Q to quit: \n""").lower()
  if r == "q":
    break
  elif r.isalpha():
    print("Sorry, incorrect input, try again.\n")
    continue
  circle_area(r)