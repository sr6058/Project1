#NAME : Smriti Ramachandran
#NET ID: sr6058


#Connect 4 game
import random
import os
import time
#--Intialisation phase--

print("--------------------")
print("   CONNECT4 GAME    ")
print("--------------------")

#dimensions of board
rows=6
columns=7
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#creation of 2D board
board = [] 
# This creates the board with the given dimension
for row in range(rows):
    row_list = []
    # 1 line/list at a time and add to board
    for col in range(columns):
        row_list.append(' ')
    board.append(row_list)


#function for printing the board displayed to the user
def printboard():
  letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

  for cols in range(columns): 
     print("   "+letters[cols], end="") #displays the columns using letters
  # do not create a newline while printing # the numbers of the  colums.
  print("\n +" + "---+" * columns)
  for row in range(rows):
     print(str(" ") + '|', end=" ")
     for col in range(columns):
         print(board[row][col] + ' | ', end="")
     print("\n +"+"---+"*columns)
printboard() #displays empty board to the user

#player info

numplayer=int(input("Enter number of players:"))
if (numplayer<=5 and numplayer>=2):
    lst=["X","O","V","H","M"]
    playerinfo={} #dictionary storing number of players and respective checkers
    for i in range(numplayer): #0,1,2
        playerinfo[i]=lst[i]
#display checker for each player
for i in playerinfo:
  print("Player:",i," Checker:",playerinfo[i])

       

#Game phase

#dropping checker in the column
def dropchecker(checker,i):
  ans="y"
  while ans=="y":
      print("Player",i,end=" ")
      nplayerinput=input("Enter column where the checker has to be dropped:")
      if nplayerinput.isalpha() and nplayerinput.isupper(): #checking whether column entered is uppercase
        nplayerinput=letters.index(nplayerinput)
        if nplayerinput<0 or nplayerinput>=columns: #checking whether the column entered is within board dimensions
            print("Invalid input! Re-enter value")
            ans="y"
        else:
            ans="n"
      else:
           print("Error! Enter column letter in uppercase!")
           ans="y"
  
  columnchosen=nplayerinput #3
  for i in range(rows-1,-1,-1):
      if board[i][columnchosen]==" ":
              board[i][columnchosen]=checker
              return i,columnchosen #drop successful
  else:
      print("Column full of checkers! Player turn invalid!")
      return -1,-1 #drop unsuccessful
#--main--

#to choose random player order
playerorder=random.sample(range(0,numplayer),numplayer) 


#checking for connect 4

def connect4check(row,columnchosen,checker):
   
   
   #horizontal check right direction
   if columnchosen+3<=columns-1: #defensive coding : to check if a horizontal connect 4 is within dimensions
       connect4counter=0
       for i in [0,1,2,3]:
         if board[row][columnchosen+i]==checker: #checking for 4 consecutive checkers
            connect4counter+=1
       if connect4counter==4:
            return 2 #there is a connect 4 in the horizontal right direction
   #horizontal check left direction
   if columnchosen-3 >=0:
       connect4counter=0
       for i in [0,1,2,3]:
         if board[row][columnchosen-i]==checker:
            connect4counter+=1
       if connect4counter==4:
            return 2 #connect 4
   
   #vertical check up
   if row+3<=rows-1:
       connect4counter=0
       for i in [0,1,2,3]:
         if board[row+i][columnchosen]==checker:
            connect4counter+=1
            
       if connect4counter==4:
            return 2
   #vertical check down
   if row-3>=0:
       connect4counter=0
       for i in [0,1,2,3]:
         if board[row-i][columnchosen]==checker:
            connect4counter+=1
       if connect4counter==4:
            return 2
   
   #diagonal check right upwards
   if row-3>=0 and columnchosen+3<=columns-1:
       connect4counter=0
       for i in [0,1,2,3]:
           if board[row-i][columnchosen+i]==checker:
              connect4counter+=1
       if connect4counter==4:
            return 2
   #diagonal check left upwards
   if row-3>=0 and columnchosen-3>=0:
       connect4counter=0
       for i in [0,1,2,3]:
           if board[row-i][columnchosen-i]==checker:
              connect4counter+=1
       if connect4counter==4:
            return 2
   #diagonal check right downwards
   if row+3<=rows-1 and columnchosen+3<=columns-1:
       connect4counter=0
       for i in [0,1,2,3]:
           if board[row+i][columnchosen+i]==checker:
              connect4counter+=1
       if connect4counter==4:
            return 2
   #diagonal check left downwards
   if row+3<=rows-1 and columnchosen-3>=0:
       connect4counter=0
       for i in [0,1,2,3]:
           if board[row+i][columnchosen-i]==checker:
              connect4counter+=1
       if connect4counter==4:
         return 2
   
   return (-2) #there is no connect 4

ro=col=0
ans1=-2
concheck="n"


while concheck=="n":
   for i in playerorder:
       if concheck=="n":
        checker=playerinfo[i] 
        ro,col=dropchecker(checker,i) #to drop the checker
        time.sleep(2) #delays output before clearing the screen 1
        os.system("clear") 
        printboard()
        if ro==-1 and col==-1: #player turn skipped
           continue
        else:
            #to check for a possible connect 4
            
            ans1=connect4check(ro,col,checker)
            
            if ans1==2:
               print("Player",i, "has won! Connect 4!")
               concheck="y"
            elif ans1!=2: #to check for a draw
                cnt=0
                for i in range(rows):
                    for j in range(columns):
                        if board[i][j] in ["X","O","V","H","M"]:
                            cnt+=1
                if cnt==(rows)*(columns):
                    print("The game is a DRAW!")
                    concheck="y"
               
            else:
               concheck="n"
                

