board=['1','2','3','4','5','6','7','8','9']
def printboard():
	print(board[0],"|",board[1],"|",board[2])
	print("---------")
	print(board[3],"|",board[4],"|",board[5])
	print("---------")
	print(board[6],"|",board[7],"|",board[8])
player1turn=True
for i in range (9):
	printboard()
#player 1 plays
	if player1turn:
		p=input("player 1, choose your place :")
		if p in board:
			board[int(p)-1]='X'
			player1turn= not player1turn			
#player 2 plays
	else:
		p=input("player 2, choose your place:")
		if p in board:
			board[int(p)-1]='O'
			player1turn=not player1turn
#winning combinations
a1=board[0,1,2]
a2=board[3,4,5]
a3=board[6,7,8]
a4=board[0,3,6]
a5=board[1,4,7]
a6=board[2,5,8]
a7=board[2,4,6]
a8=board[0,4,8]
if(a1=='X' or a2=='X' or a3=='X' or a4=='X' or a5=='X' or a6=='X' or a7=='X' or a8=='X'):
	print("player one wins")
elif(a1=='O' or a2=='O' or a3=='O' or a4=='O' or a5=='O' or a6=='O' or a7=='O' or a8=='O'):
	print("player 2 wins")
else:
	print("it's a tie")