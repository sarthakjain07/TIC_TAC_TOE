# Global variables

# this is a platform where the game will be played
platform=["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

# If game is still going on
goingOn=True

# winner or tied or loser
winner=None
loser=None

# who's turn is it?
currentPlayer="X"

# This function displays the platform of Game
def displayplatform():
  print(" | "+platform[0]+" | "+platform[1]+" | "+platform[2]+" | ")
  print(" | "+platform[3]+" | "+platform[4]+" | "+platform[5]+" | ")
  print(" | "+platform[6]+" | "+platform[7]+" | "+platform[8]+" | ")

# This function checks the rows of platform
def checkRows():
  # Using global variable in this function
  global goingOn

  # Checking if rows have common value and is not empty
  row_1=platform[0]==platform[1]==platform[2]!="-"
  row_2=platform[3]==platform[5]==platform[6]!="-"
  row_3=platform[6]==platform[7]==platform[8]!="-"  

  # Stopping the game when one has won
  if row_1 or row_2 or row_3:
    goingOn=False

  # Returning the winner 
  if row_1:
    return platform[0]
  elif row_2:
    return platform[3]
  elif row_3:
    return platform[6]
  else:
    return        

# This function checks the columns of platform
def checkColumns():
    # Using global variable in this function
  global goingOn

  # Checking if columns have common value and is not empty
  column_1=platform[0]==platform[3]==platform[6]!="-"
  column_2=platform[1]==platform[4]==platform[7]!="-"
  column_3=platform[2]==platform[5]==platform[8]!="-"  

  # Stopping the game when one has won
  if column_1 or column_2 or column_3:
    goingOn=False

  # Returning the winner 
  if column_1:
    return platform[0]
  elif column_2:
    return platform[1]
  elif column_3:
    return platform[2]
  else:
    return

# This function checks the diagonals of platform
def checkDiagonals():
    # Using global variable in this function
  global goingOn

  # Checking if diagonals have common value and is not empty
  diagonal_1=platform[0]==platform[4]==platform[8]!="-"
  diagonal_2=platform[6]==platform[4]==platform[2]!="-" 

  # Stopping the game when one has won
  if diagonal_1 or diagonal_2:
    goingOn=False

  # Returning the winner 
  if diagonal_1:
    return platform[0]
  elif diagonal_2:
    return platform[6]
  else:
    return

# This function checks if the player wins
def ifWin():

  # Setting global variable in function
  global winner

  # checking rows
  rowWinner=checkRows()

  # checking columns
  columnWinner=checkColumns()

  # checking diagonals
  diagonalWinner=checkDiagonals()

  if rowWinner:
    winner=rowWinner
  elif columnWinner:
    winner=columnWinner
  elif diagonalWinner:
    winner=diagonalWinner
  else:
    winner=None

# This function tells whether the game is over
def gameOver():
  ifWin()
  ifTie()
  
# This function checks whether the game is tied
def ifTie():

  # Using global variable in this function
  global goingOn

  # Condition of match in case Tie
  if "-" not in platform:
    goingOn=False

# This function changes the player
def changePlayer():
  # Using global variable in function 
  global currentPlayer

  # Flipping the players from X to O & vice versa
  if currentPlayer=="X":
    currentPlayer="O"
  elif currentPlayer=="O":
    currentPlayer="X"

# This function handles the turns of players one by one
def handleTurns(player):

  print(player + "'s turn'")

  # taking the input of position
  position=int(input("Choose a position from 1-9: "))-1

  while position not in [0,1,2,3,4,5,6,7,8]:
    position=int(input("Invalid choice! Choose a position again from 1-9: "))-1
  
  # position=position-1


  while platform[position]!="-":
    print("Already filled. Try another place")
    position=int(input("Choose a position again from 1-9: "))-1  
  
  platform[position]=player
  displayplatform()

# This function operates the game
def playGame():
  # Displaying the platform initially
  displayplatform()
  # The game is still going on with the loop
  while goingOn:
    # handling turns of players one by one
    handleTurns(currentPlayer)
    # checking if the game is over
    gameOver()
    # changing the player according to their chance
    changePlayer()

  # When the game is ended
  if winner == "X" or winner=="O":
    print("Winner is " + winner)
  elif winner == None:
    print("Match Tied.")    

if __name__=="__main__": 
  playGame()          

