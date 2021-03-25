from gameComponents import gameVars

# define a win or lose function (version 1)
#def winorlose(status):
	#version 1 of function
	# print("Inside winorlose function; status is: ", status)
	#print("You", status, "! Would you like to play again?")
	#choice = input("Y / N? ")

	#if choice =="N" or choice == "n":
	#	print("You chose to quit! Better luch next time!")
	#	exit()
	#elif choice == "Y" or choice == "y":
		# reset the player and computer lives
		# and reset player choice to Flase, so our loop restarts

# Define a win / lose function and refer to it (invoke it) in our game loop

def winorlose(status):
	if status == "won":
		pre_message = "DAAAMN BUOI! YOU GOT IT!"
	else:
		pre_message = "NAH! YOU'RE SUCH A LOOOSERR!"

	print(pre_message + 'But yeah it is just a game right? Would you like to play again?')

	choice = False

	while choice == False:
		choice = input("Y / N? ")

		if choice == "Y" or choice == "y":
			#reset the game loop and start over again
			#global player_lives
			#global computer_lives
			#global total_lives

			#it's commented because now we are updating the variables from gameVars

			gameVars.player_lives = gameVars.total_lives
			gameVars.computer_lives = gameVars.total_lives
			gameVars.player_choice = False
	
		elif choice == "N" or choice == "n":
			#exit message and quit
			print("As you are DAMN WEAK You chose to quit. See you when I see you Warrior!")
			exit()
		else:
			print("Please choose it right bro, I dont have the whole day - Y or N")
			choice = False
	#old code:
		#else:
		#	print("Make a valid choice - Y or N")
		#	#this might generate a bug that we need to fix later
		#	choice = input("Y / N? ")