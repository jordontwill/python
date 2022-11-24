# Choice Game
choice1 = input("left or right?\n").lower()

if choice1 == "left":
  choice2 = input("up or down?\n").lower()
  if choice2 == "up":
    choice3 = input("red or blue?\n").lower()
    if choice3 == "red":
      print("You found the treasure!")
    else:
      print("game over.")
  else:
    print("game over.")
else:
  print("Game over.")
  
  
