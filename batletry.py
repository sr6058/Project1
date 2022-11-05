#Name : Smriti Ramachandran
#Net ID : sr6058 , Student ID : N12909777



import random #imports the random module
import os     #imports the os module
import time   #imports the time module

print(" ----------------------- ")
print("  WELCOME TO BATTLESHIP  ")
print(" ----------------------- ")
print()
SHIP_SIZE=int(input("Enter size of the ship:"))
DIMENSION=int(input("Enter dimension of the board:"))

while( (SHIP_SIZE < 2 or SHIP_SIZE>4) or (DIMENSION >10  or DIMENSION<4)) : #checking for correct value of ship size and dimension

  if (SHIP_SIZE < 2 or SHIP_SIZE>4):
      print("Invalid input! Please enter ship size between 2 and 4")
      SHIP_SIZE=int(input("Enter size of the ship:"))
      
  if (DIMENSION >10  or DIMENSION<4):
      print("Invalid input! Please enter dimension lesser than 10")
      DIMENSION=int(input("Enter dimension of the board:"))
      

    
#creation of the 2D board : MAIN
board = []
# This creates the board with the given dimension
for row in range(DIMENSION):
    row_list = []
    # 1 line/list at a time and add to board
    for col in range(DIMENSION):
        row_list.append(' ')
    board.append(row_list)



#function for printing the board displayed to the user
def printboard():
  letters=["A","B","C","D","E","F","G","H","I","J"]

  for cols in range(DIMENSION): 
     print("   "+letters[cols], end="") #displays the columns using letters
  # do not create a newline while printing # the numbers of the  colums.
  print("\n +" + "---+" * DIMENSION)
  for row in range(DIMENSION):
     print(str(row) + '|', end=" ")
     for col in range(DIMENSION):
         print(board[row][col] + ' | ', end="")
     print("\n +"+"---+"*DIMENSION)


#creation of the hidden board
hidden_board = []
# This creates the hidden board with the given dimension
for row in range(DIMENSION):
    row_list = []
    # 1 line/list at a time and add to board
    for col in range(DIMENSION):
        row_list.append(' ')
    hidden_board.append(row_list)

#printing the hidden  board
def printhiddenboard():
  letters=["A","B","C","D","E","F","G","H","I","J"]


  for cols in range(DIMENSION): #chng to letters
    print("   "+letters[cols], end="")
  # do not create a newline while printing # the numbers of the colums.
  print("\n +" + "---+" * DIMENSION)
  for row in range(DIMENSION):
     print(str(row) + '|', end=" ")
     for col in range(DIMENSION):
         print(hidden_board[row][col] + ' | ', end="")
     print("\n +"+"---+"*DIMENSION)




#creating a random ship on the hidden board
#0-down , 1- right
orientation=random.randint(0,1) #chooses a random orientation

if orientation==0:
    randcol=random.randint(0,DIMENSION-1) # As the orientation is down, any column within the dimension can be chosen
    randrow=random.randint(0,DIMENSION-SHIP_SIZE) # chooses random row with given condition
    for i in range(0,SHIP_SIZE):
        hidden_board[randrow][randcol]="X"
        randrow+=1

elif orientation==1:
    randrow=random.randint(0,DIMENSION-1) #As the orientation is right, row can be within dimension
    randcol=random.randint(0,DIMENSION-SHIP_SIZE) #chooses random column with given condition
   
    for i in range(0,SHIP_SIZE):
        hidden_board[randrow][randcol]="X"
        randcol+=1
        
#--Game Phase---

hit_count=0 #counter variable to check is ship size is hit
numguess=0 #counter variable to keep track of the number of guesses

#function to ask user for guess
r=c=0
def guess(r,c):
  val=True
  letter=["A","B","C","D","E","F","G","H","I","J"]
  #Takes valid input for the guess from the user
  while val==True:
    guess=input("Enter your guess in the format CR (Column, Row) : ")
    nguess=guess.upper()
    if nguess[0].isalpha() and nguess[1].isdigit() and (0<=int(nguess[1])< DIMENSION) and (0<=int(letter.index(nguess[0]))<DIMENSION):

      columng=int(letter.index(nguess[0]))
      rowg=int(nguess[1])
      val=False
    
    else:
      print("Enter valid guess!")
      val=True
  return rowg,columng



#--processing valid user input--
print("GAME BOARD")
print()
printboard()
while hit_count!=SHIP_SIZE:
  
  rowg,columng=guess(r,c)
  if board[rowg][columng]=="#":
    print("Position previously guessed! Try Again!")
  elif hidden_board[rowg][columng]=="X":
    board[rowg][columng]="X"
    print("Correct Guess!")
    hit_count+=1
  else:
    board[rowg][columng]="#"
  numguess+=1 #increments the number of guesses
  
  time.sleep(2) #delays output before clearing the screen
  os.system("clear") #clears the screen
  print("BATTLESHIP GAME\n")
  printboard() #prints the user board
  print("Number of guesses/ Score:",numguess)
  print()
  

print("Congrats! You've WON!!")  
print("----GAME OVER----")
    

