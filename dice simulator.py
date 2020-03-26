#dice simulator
import random as r  								#because I am lazy 

print('Dice simulator by Midhun B M') 				#Mandatory credits :P
print('-----------------------------')

char = input('Press y to roll the dice : ')			#User input
while (char=='y' or char == 'Y'):				
	dice = r.randint(1,6)							#Generate random no
	if (dice == 1):									#If statements will display die face for the coreesponding number
		print('---------')
		print('-       -')
		print('-       -')	
		print('-   0   -')
		print('-       -')
		print('-       -')
		print('-       -')	
		print('---------')

	if (dice == 2):
		print('---------')
		print('-       -')	
		print('-   0   -')
		print('-       -')
		print('-       -')
		print('-   0   -')
		print('-       -')	
		print('---------')

	if (dice == 3):
		print('---------')
		print('-       -')	
		print('-   0   -')
		print('-       -')
		print('-   0   -')
		print('-       -')
		print('-   0   -')	
		print('---------')

	if (dice == 4):
		print('---------')
		print('-       -')	
		print('- 0   0 -')
		print('-       -')
		print('-       -')
		print('-       -')
		print('- 0   0 -')	
		print('---------')
	if (dice == 5):
		print('---------')
		print('-       -')	
		print('- 0   0 -')
		print('-       -')
		print('-   0   -')
		print('-       -')
		print('- 0   0 -')	
		print('---------')	
	if (dice == 6):
		print('---------')
		print('-       -')	
		print('- 0   0 -')
		print('-       -')
		print('- 0   0 -')
		print('-       -')
		print('- 0   0 -')	
		print('---------')	

	char = input("press y to roll again : ")			# Rereoll