# This function displays the platform of Game
def displayplatform(platform):
  print(" | "+platform[0]+" | "+platform[1]+" | "+platform[2]+" | ")
  print(" | "+platform[3]+" | "+platform[4]+" | "+platform[5]+" | ")
  print(" | "+platform[6]+" | "+platform[7]+" | "+platform[8]+" | ")

# This function handles the turns
def handleTurns(platform):
  position=int(input("Choose a position from 1-9: "))-1
  platform[position]="X"
  displayplatform(platform)

# This function operates the game
def playGame(platform):
  displayplatform(platform)
  handleTurns(platform)

if __name__=="__main__": 
  platform=["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]

  playGame(platform)          

