# importing a package to extend python (just like we extended Sublime, Atom or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose

gameVars.player_choice == False
while gameVars.player_choice is False: #
	print("=====================*/ RPS GAME */===================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("======================================================")
	# Version 1, to explain array indexing
	#player_choice = choices[1]
	#print("index 1 in the choice array is " + player_choice + ", which is paper")
	print("Choose your weapon! Or type quit to exit\n") #\n means "new line"

	gameVars.player_choice = input("Choose rock, paper, or scissors: \n")
	# player_choice now equals TRUE -> it has a value

	if gameVars.player_choice == "quit":
		print("You chose to quit!")
		exit()

	print("User chose: " + gameVars.player_choice)

	# This will be the AI choice -> a random pick from the choices array
	gameVars.computer_choice = gameVars.choices[randint (0, 2)]

	print("Computer chose: " + gameVars.computer_choice)

	if gameVars.computer_choice == gameVars.player_choice:
		print("Tie!")

	elif gameVars.computer_choice == "rock":
		if gameVars.player_choice == "scissors":
			print("You lose!")
			#verbose way
			#player_lives = player_lives - 1
			#simplified way
			gameVars.player_lives -= 1
		else:
			print("You win!")
			gameVars.computer_lives -= 1

	elif gameVars.computer_choice == "paper":
		if gameVars.player_choice == "scissors":
			print("You win!")
			gameVars.computer_lives -= 1
		else:
			print("You lose!")
			gameVars.player_lives -= 1

	elif gameVars.computer_choice == "scissors":
		if gameVars.player_choice == "paper":
			print("You lose!")
			gameVars.player_lives -= 1

		else:
			print("You win!")
			gameVars.computer_lives -= 1

	if gameVars.player_lives == 0:
		winLose.winorlose("lose")

	if gameVars.computer_lives == 0:
		winLose.winorlose("won")
		

	#print("player_lives:", gameVars.player_lives)
	#print("computer_lives:", gameVars.computer_lives)

	# make the loop keep running by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True

	gameVars.player_choice = False






