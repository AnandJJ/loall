#to obtain an output where a key can generate a random number and another key to exit the program
import random
print("here you go",random.randint(1,100))
while True:
	a=input("press 'r' to retry")
	if(a=='r'):
		print("here you go",random.randint(1,100))
		a=input("press 'q' to quit")
	elif(a=='q'):
		print("bye")
		exit()
	


	



	
     


