import random
d={1:'rock',2:'paper',3:'scissor'}
c=d[random.randint(1,3)]
while(True):
	u=input("enter 'rock','paper' or 'scissor' or 'q' to quit the game")
	if(c=='rock' and u=='scissor' or c=='scissor' and u=='paper' or c=='paper' and u=='rock'):
		print(c,"computer wins")
	elif(c=='rock' and u=='rock' or c=='scissor' and u=='scissor' or c=='paper' and u=='paper'):
		print(c,"its a tie")
	elif(c=='scissor' and u=='rock' or c=='paper' and u=='scissor' or c=='rock' and u=='paper'):
		print(c,"player wins")
	elif(u=='q'):
		print("game over")
		exit()
	else:
		print("don't enter unnecessary characters")
		exit()