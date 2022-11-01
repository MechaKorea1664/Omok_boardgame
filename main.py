import gameBoard
import credits


data=gameBoard.boardData(0)
menu=gameBoard.menu(0)
player_input=gameBoard.playerInput(1)
turn=1
menu.logo()
menu.listMenu()
player_select=(int(input('\nGo to ')))
while player_select!=-1:
  if player_select>5 or player_select<-1:
    print('//ERROR: Invalid choice. Please choose from given choices.//')
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
  player_select=menu.chooseMenu(player_select)
  print('\n\n\n')
  if player_select!=-1:
    menu.logo()
    menu.listMenu()
    player_select=(int(input('\nGo to ')))
while True:
  print('Instructions / How to Play:\n\nOmok is played with 2 players, each with white and black moks.\nIn order to win, you have to connect 5 of your mok in a row.\nIt has to be in a straight line, either horizontally,\nvertically, or diagonally\n\nBelow, you can choose the dimensions of the board.\nThe max width and height is 15.\n\nHave fun!\n\n')
  print('Choose the dimensions of the board.\n\n')
  w = int(input('Board width? '))
  h = int(input('Board height? '))
  if w > 15 or h > 15:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('//ERROR: Max value of width and height is restricted to 15.//\n')
  else:
    gameboard = gameBoard.gameBoard(w, h, False)
    gameboard.newPage()
    gameboard.drawBoard()
    break
print('|'+player_input.returnCurrentPlayer()+"'s turn|"+player_input.returnCurrentPlayer()+"'s Mok: "+player_input.returnCurrentPlayerMok()+' |Turn '+str(turn)+'|')
while True:      #
  while True:    #sets move value to row and column
    while True:  #asks for move input on repeat
      move=str(input('Your move: '))
      if len(list(move))>3 or len(list(move))<2:
        print('//ERROR: Missing information. Correct format: <row><column>; Example: k5; Not case sensitive//')
      else:
        break
    row=list(move)[0]
    if len(list(move))==2:
      column=list(move)[1]
    elif len(list(move))==3:
      column=list(move)[1]+list(move)[2]
    if not row.upper() in gameBoard.alphabet or gameBoard.alphabet.index(row.upper())<1 or gameBoard.alphabet.index(row.upper())>h:
      print('//ERROR: Row is out of range. Correct format: <row><column>; Example: k5; Not case sensitive//')
    elif not column in gameBoard.number or type(column)!=str or int(column)<1 or int(column)>w:
      print('//ERROR: Column is out of range. Correct format: <row><column>; Example: k5; Not case sensitive//')
    else:
      break
  if player_input.placeMok(row,column)!=False and player_input.checkOmokHorizontal()==False and player_input.checkOmokVertical(h)==False and player_input.checkOmokDiagonalRtoL(w,h)==False and player_input.checkOmokDiagonalLtoR(w,h)==False and player_input.checkStalemate(w,h)==False:
    player_input.placeMok(row,column)
    turn+=1
    for i in range(h+1):  
      print('\t'.join(data.returnRowInput(i))+'\n')
    player_input.checkOmokHorizontal()
    player_input.checkOmokVertical(h)
    player_input.checkOmokDiagonalRtoL(w,h)
    player_input.checkOmokDiagonalLtoR(w,h)
    player_input.checkStalemate(w,h)
    player_input.changePlayer()
    print('|Player '+str(player_input.returnCurrentPlayer())+"'s turn|Player "+str(player_input.returnCurrentPlayer())+"'s Mok: "+player_input.returnCurrentPlayerMok()+' |Turn '+str(turn)+'|')
  elif player_input.placeMok(row,column)==False and player_input.checkOmokHorizontal()==False and player_input.checkOmokVertical(h)==False and player_input.checkOmokDiagonalRtoL(w,h)==False and player_input.checkOmokDiagonalLtoR(w,h)==False and player_input.checkStalemate(w,h)==False:
    print('//ERROR: Mok is already there!//')
    print('|'+player_input.returnCurrentPlayer()+"'s turn|"+player_input.returnCurrentPlayer()+"'s Mok: "+player_input.returnCurrentPlayerMok()+' |Turn '+str(turn)+'|')
  else:
    print('\n\n\n\n')
    print(credits.gameOver)
    for i in range(h+1):  
      print('\t'.join(data.returnRowInput(i))+'\n')
    break
if player_input.checkOmokHorizontal()==1 or player_input.checkOmokVertical(h)==1 or player_input.checkOmokDiagonalRtoL(w,h)==1 or player_input.checkOmokDiagonalLtoR(w,h)==1:
  print(player_input.returnPlayerNick(1)+' Wins!\n\n'+player_input.returnPlayerNick(1)+' has conquered the board in '+str(turn)+' turns!')
elif player_input.checkOmokHorizontal()==2 or player_input.checkOmokVertical(h)==2 or player_input.checkOmokDiagonalRtoL(w,h)==2 or player_input.checkOmokDiagonalLtoR(w,h)==2:
  print(player_input.returnPlayerNick(2)+' Wins!\n\n'+player_input.returnPlayerNick(2)+' has conquered the board in '+str(turn)+' turns!')
elif player_input.checkStalemate(w,h)==True:
  print('Stalemate! Even after '+str(turn)+' turns, no one managed to win!')
else:
  print('No one wins, due to an unexpected error!')