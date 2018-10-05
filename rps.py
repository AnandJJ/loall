import random
d={1:'r',2:'p',3:'s'}
c=d[random.randint(1,3)]
u=input("enter 'r','p' or 's'")
if(c=='r' and u=='s' or c=='s' and u=='p' or c=='p' and u=='r'):
	print(c,"computer wins")
elif(c=='r' and u=='r' or c=='s' and u=='s' or c=='p' and u=='p'):
	print(c,"its a tie")
else:
	print(c,"player wins")
	exit()
