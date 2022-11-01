import random
import credits

row0 = [' ']
row1 = ['A']
row2 = ['B']
row3 = ['C']
row4 = ['D']
row5 = ['E']
row6 = ['F']
row7 = ['G']
row8 = ['H']
row9 = ['I']
row10 = ['J']
row11 = ['K']
row12 = ['L']
row13 = ['M']
row14 = ['N']
row15 = ['O']
rowAll=[row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15]
mok=['·','⬬','⬭']
playerNick=['','Player 1','Player 2']
alphabet=['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
randName=['','PLAYAH','0M0K','오목','LMAOmok','Progamer','OmokomO','Mokbang','komO','CoffeeMokka','newbie','Prof. Mok','OhMyMok','ggez','replit','SuperiorPython','hello','Kerbonaut1664','grassToucher','GigaMok','Baduk','textbased','redditor','OmokStan',':nerd:','HELPME','AAHHHH','OmokEnjoyer','mokmok','ezpz_lemon_sqz','Sgt. Omok','CheckSlug','Omok_JunPro','PD GreatOmok','INDIYAAAA','basedIndividual','RussianRoulette','Connect5','LOLlipop','GrandMaster','0mokK1nG','RealTimeSleep','OmoKorea','MokDonalds','BlkNWht','Hello World!','...---...','boredGame']
class boardData:
    def __init__(self, h):
        self.height = h
    def change_h(self, new_h):
        self.height = new_h
    def returnRow(self):
        num_list = self.height
        return rowAll[num_list]
    def returnRowInput(self,num_input):
        return rowAll[num_input]
    def printAllRow(self):  #for troubleshooting
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        print(row6)
        print(row7)
        print(row8)
        print(row9)
        print(row10)
        print(row11)
        print(row12)
        print(row13)
        print(row14)
        print(row15)


class gameBoard:
    def __init__(self, w, h, existance):
        self.width = w
        self.height = h
        self.existance = existance
    def drawBoard(self):
        num_rows=0
        board=boardData(0)
        self.existance = True
        for i in range(self.height + 1):
            for u in range(self.width):
                if board.returnRow() == row0:
                    board.returnRow().append(str(u + 1))
                else:
                    board.returnRow().append(mok[0])
            print('\t'.join(board.returnRow()) + '\n')
            num_rows += 1
            board.change_h(num_rows)
    def newPage(self):
        num_newline = 40 - self.height + 1
        for i in range(num_newline):
            print('\n')
    def proveExistance(self):
      bool_existance=self.existance  
      return bool_existance


class menu:
    def __init__(self, player_choice):
        self.choice = player_choice
    def logo(self):
        print('   _|_|    _|      _|    _|_|    _|    _|  \n _|    _|  _|_|  _|_|  _|    _|  _|  _|    \n _|    _|  _|  _|  _|  _|    _|  _|_|      \n _|    _|  _|      _|  _|    _|  _|  _|    \n   _|_|    _|      _|    _|_|    _|    _|  \n\n\nKorean Traditional Board Game - Made by Kevin\n\n\n\n')
    def listMenu(self):
        list_menu = ['Welcome to Omok! Would you like to...', '1. Start a new game','2. Customize your pieces', '3. Customize player names', '4. Look at the credits','5. Hear a joke', '6. Quit']
        print('\n'.join(list_menu))
    def chooseMenu(self, new_choice):
      self.choice=new_choice  
      player_select = self.choice
      if player_select == 1:
          return -1
      elif player_select == 2:
          print('==========MOK CHANGER==========\n')  
          print('Current Mok of '+playerNick[1]+': '+mok[1]+'\nCurrent Mok of '+playerNick[2]+': '+mok[2]+'\nCurrent Default Mok: '+mok[0]+'\n')
          change=input("Would you like to customize your pieces? Enter...\n1: Customize "+playerNick[1]+"'s mok\n2: Customize "+playerNick[2]+"'s mok\n3: Customize Default mok\n4: Back to Main Menu\n(to note, you cannot copy/paste symbols here. Search online for 'alt codes' for Windows/Mac)\n\nGo to ")
          while True:
            if not change in number or int(change)<1 or int(change)>4:
              print('//ERROR: Input out of range//')
              print('\n\nCurrent Mok of '+playerNick[1]+': '+mok[1]+'\nCurrent Mok of '+playerNick[2]+': '+mok[2]+'\nCurrent Default Mok: '+mok[0]+'\n')
              change=input("Would you like to customize your pieces? Enter...\n1: Customize "+playerNick[1]+"'s mok\n2: Customize "+playerNick[2]+"'s mok\n3: Customize Default mok\n4: Back to Main Menu\n(to note, you cannot copy/paste symbols here. Search online for 'alt codes' for Windows/Mac)\n\nGo to ")
            else:
              break
          if int(change)==1:
            mok1_input=input("Enter "+playerNick[1]+"'s new mok: ")
            while True:
              if len(list(mok1_input))!=1:
                print('Please only enter 1 character.')
                mok1_input=input("Enter "+playerNick[1]+"'s new mok: ")
              else:
                break
            mok[1]=mok1_input
          elif int(change)==2:
            mok2_input=input("Enter "+playerNick[2]+"'s new mok: ")
            while True:
              if len(list(mok2_input))!=1:
                print('Please only enter 1 character.')
                mok2_input=input("Enter "+playerNick[2]+"'s new mok: ")
              else:
                break
            mok[2]=mok2_input
          elif int(change)==3:
            mok0_input=input("Enter the new Default mok: ")
            while True:
              if len(list(mok0_input))!=1:
                print('Please only enter 1 character.')
                mok0_input=input("Enter the new Default mok: ")
              else:
                break
            mok[0]=mok0_input
          else:
            pass
      elif player_select == 3:
        while True:
          print('\n\n\n\n==========NAME CHANGER==========\n\nCurrent names:\n\tPlayer 1: '+playerNick[1]+'\n\tPlayer 2: '+playerNick[2])
          print('\n\nWould you like to...\n\t1. Change name for Player 1\n\t2. Change name for Player 2\n\t3. Get a random name \t(**FOR BOTH PLAYERS**)\n\t4. Reset to default \t(**FOR BOTH PLAYERS**)\n\t5. Exit to Main Menu\n\n')
          nameChangeSelect=int(input('Go to '))
          if nameChangeSelect<1 or nameChangeSelect>5:
            print('//ERROR: Input out of range//')
          elif nameChangeSelect==1:
            playerNickNew1=str(input('\nEnter '+playerNick[1]+"'s new name: "))
            playerNick[1]=playerNickNew1
          elif nameChangeSelect==2:
            playerNickNew2=str(input('\nEnter '+playerNick[2]+"'s new name: "))
            playerNick[2]=playerNickNew2
          elif nameChangeSelect==3:
            randNameNum1=random.randint(1,len(randName)-1)
            playerNick[1]=randName[randNameNum1]
            randNameNum2=random.randint(1,len(randName)-1)
            while randNameNum1==randNameNum2:
              randNameNum2=random.randint(1,len(randName)-1)
            playerNick[2]=randName[randNameNum2]
          elif nameChangeSelect==4:
            playerNick[1]='Player 1'
            playerNick[2]='Player 2'
          elif nameChangeSelect==5:
            break
      elif player_select == 4:
          print(credits.credits)
          credit_input=input('1: Back to Main Menu\nGo to ')
          while True:
            if not credit_input in number or number.index(credit_input)!=1:
              print("You missed the '1' key? HOW?\n\n")
              credit_input=input('1: Back to Main Menu\nGo to ')
            else:
              break
          pass
      elif player_select == 5:
            joke_response = ['My grades', 'My sleep schedule', 'My bank account', 'Python','C++', 'Javascript']
            joke_reaction = ['lol', 'LOL', 'ha', 'haha', 'HAHAHA', 'funny, right?',"ehh, this one wasn't funny at all"]
            print("Here's the joke: "+str(joke_response[random.randint(0, 5)])+', '+str(joke_reaction[random.randint(0, 6)]) + '!')
      elif player_select == 6:
            exit_response = ['See ya', 'Bye', 'Bye bye', 'GG', '잘가', 'Cya', 'Later']
            print(str(exit_response[random.randint(0, 6)]) + '!')
            exit()


class playerInput:
  def __init__(self,num_player):
    self.currentPlayer=num_player
  def changePlayer(self):
    if self.currentPlayer==1:
      self.currentPlayer=2
    elif self.currentPlayer==2:
      self.currentPlayer=1
  def placeMok(self,row,column):
    self.targetRow=rowAll[alphabet.index(row.upper())]
    self.targetColumn=int(column)
    self.currentPlayer
    if self.targetRow[self.targetColumn]!=mok[0]:
      return False
    elif self.currentPlayer==1:
      self.targetRow[self.targetColumn]=mok[1]
    elif self.currentPlayer==2:
      self.targetRow[self.targetColumn]=mok[2]
  def returnCurrentPlayer(self):
    return playerNick[self.currentPlayer]
  def returnPlayerNick(self,playerNum):
    return playerNick[playerNum]
  def returnCurrentPlayerMok(self):
    if self.currentPlayer==1:
      return mok[1]
    elif self.currentPlayer==2:
      return mok[2]
    else:
      return mok[0]
  def checkOmokHorizontal(self):
    omok_player1_hori=0
    omok_player2_hori=0
    while True:
      for i in range(len(self.targetRow)):
        if self.currentPlayer==1 and omok_player1_hori<5:
          if self.targetRow[i]!=mok[1]:
            omok_player1_hori=0
          else:
            omok_player1_hori+=1
        if self.currentPlayer==2 and omok_player2_hori<5:
          if self.targetRow[i]!=mok[2]:
            omok_player2_hori=0
          else:
            omok_player2_hori+=1
      break
    if omok_player1_hori==5:
      return 1
    elif omok_player2_hori==5:
      return 2
    else:
      return False
  def checkOmokVertical(self,column):
    column=int(column)
    omok_player1_vert=0
    omok_player2_vert=0
    while True:
      for i in range(column+1):
        row=rowAll[i]
        mokAtColumn=row[self.targetColumn]
        if self.currentPlayer==1 and omok_player1_vert<5:
          if mokAtColumn!=mok[1]:
            omok_player1_vert=0
          else:
            omok_player1_vert+=1
        if self.currentPlayer==2 and omok_player2_vert<5:
          if mokAtColumn!=mok[2]:
            omok_player2_vert=0
          else:
            omok_player2_vert+=1
      break
    if omok_player1_vert==5:
      return 1
    elif omok_player2_vert==5:
      return 2
    else: 
      return False
  def checkOmokDiagonalRtoL(self,w,h): #Checks Diagonal Right to Left
    omok_player1_diagRtoL=0
    omok_player2_diagRtoL=0
    distance_from_right=w-self.targetColumn+1
    distance_from_left=self.targetColumn
    start_pos_row=rowAll.index(self.targetRow)
    start_pos_column=self.targetColumn
    while start_pos_row>1 and start_pos_column<w: #sets the scan starting positon to the diagonal top right, 
      start_pos_row-=1                            #with current mok position as origin.
      start_pos_column+=1
    if self.currentPlayer==1 and rowAll[start_pos_row][start_pos_column]==mok[1]:
      omok_player1_diagRtoL+=1
    else:
      omok_player1_diagRtoL=0
    if self.currentPlayer==2 and rowAll[start_pos_row][start_pos_column]==mok[2]:
      omok_player2_diagRtoL+=1
    else:
      omok_player2_diagRtoL=0
    while start_pos_row<h and start_pos_column>1 and omok_player1_diagRtoL<5 and omok_player2_diagRtoL<5:
      start_pos_row+=1
      start_pos_column-=1
      if self.currentPlayer==1 and rowAll[start_pos_row][start_pos_column]==mok[1]:
        omok_player1_diagRtoL+=1
      else:
        omok_player1_diagRtoL=0
      if self.currentPlayer==2 and rowAll[start_pos_row][start_pos_column]==mok[2]:
        omok_player2_diagRtoL+=1
      else:
        omok_player2_diagRtoL=0
    if omok_player1_diagRtoL>=5:
      return 1
    elif omok_player2_diagRtoL>=5:
      return 2
    else:
      return False
  def checkOmokDiagonalLtoR(self,w,h): #Checks Diagonal Left to Right
    omok_player1_diagLtoR=0
    omok_player2_diagLtoR=0
    distance_from_right=w-self.targetColumn+1
    distance_from_left=self.targetColumn
    start_pos_row=rowAll.index(self.targetRow)
    start_pos_column=self.targetColumn
    while start_pos_row>1 and start_pos_column>1: #sets the scan starting positon to the diagonal top left, 
      start_pos_row-=1                            #with current mok position as origin.
      start_pos_column-=1
    if self.currentPlayer==1 and rowAll[start_pos_row][start_pos_column]==mok[1]:
      omok_player1_diagLtoR+=1
    else:
      omok_player1_diagLtoR=0
    if self.currentPlayer==2 and rowAll[start_pos_row][start_pos_column]==mok[2]:
      omok_player2_diagLtoR+=1
    else:
      omok_player2_diagLtoR=0
    while start_pos_row<h and start_pos_column<w and omok_player1_diagLtoR<5 and omok_player2_diagLtoR<5:
      start_pos_row+=1
      start_pos_column+=1
      if self.currentPlayer==1 and rowAll[start_pos_row][start_pos_column]==mok[1]:
        omok_player1_diagLtoR+=1
      else:
        omok_player1_diagLtoR=0
      if self.currentPlayer==2 and rowAll[start_pos_row][start_pos_column]==mok[2]:
        omok_player2_diagLtoR+=1
      else:
        omok_player2_diagLtoR=0
    if omok_player1_diagLtoR>=5:
      return 1
    elif omok_player2_diagLtoR>=5:
      return 2
    else:
      return False
  def checkStalemate(self,w,h):
    count_mok0=0
    for i in range(h):
      for u in range(w):
        if rowAll[i+1][u+1]==mok[0]:
          count_mok0+=1
        else:
          pass
    if count_mok0==0:
      return True
    else:
      return False
      