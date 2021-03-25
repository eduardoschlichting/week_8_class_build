# importing a package to extend python (just like we extended Sublime, Atom or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose, compFunc

gameVars.player_choice == False





print("=====================*/ RPS GAME */=====================")
print(" Hello Warrior!!! So excited to have you here! Welcome to the Rock, Paper or Scissors Battle of the millenium!!")
print(" So, the rules are simple: win or DIE! hehe kidding...or maybe I am not... who knows?\n")
print("=====================*/ HERE ARE THE MODAFOKIN RULES */=====================\n")
print(" You start the game with 3 lifes, as you play, you may lose some, but you have to be smarter than your opponent okay?!")
print(" You MUST choose the right weapon! We know the drill: rock beats scissors, paper beats rock (that never made sense to me but okay) and so on, so be clever!\n")

while gameVars.player_choice is False:
	
	print("======================================================")
	print(" Your chances to live:", gameVars.player_lives, "/", gameVars.total_lives)
	print(" Your opponent chances to live:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("======================================================")
	# Version 1, to explain array indexing
	#player_choice = choices[1]
	#print("index 1 in the choice array is " + player_choice + ", which is paper")
	print(" Are you ready?! So choose your weapon! Or type quit to exit :) \n") #\n means "new line"

	gameVars.player_choice = input(" Choose rock, paper, or scissors: \n")
	# player_choice now equals TRUE -> it has a value

	if gameVars.player_choice == "quit":
		print(" You chose to quit! Such a WEAK! Bye!")
		exit()

	print(" Your BADASS weapon IS: " + gameVars.player_choice)

	# This will be the AI choice -> a random pick from the choices array
	gameVars.computer_choice = gameVars.choices[randint (0, 2)]

	print(" Your opponent BLEH weapon IS: " + gameVars.computer_choice)

	

	if gameVars.computer_choice == gameVars.player_choice:
		compFunc.comparison("game_tie")

	elif gameVars.computer_choice == "rock":
		if gameVars.player_choice == "scissors":
			compFunc.comparison("player_lose")
		else:
			#print(" You win! Nice one Warrior!")
			#gameVars.computer_lives -= 1
			compFunc.comparison("player_won")

	elif gameVars.computer_choice == "paper":
		if gameVars.player_choice == "scissors":

			compFunc.comparison("player_won")
			#print(" You win! Nice one Warrior!")
			#gameVars.computer_lives -= 1
		else:
			#print(" You lose! So bad!")
			#gameVars.player_lives -= 1

			compFunc.comparison("player_lose")


	elif gameVars.computer_choice == "scissors":
		if gameVars.player_choice == "paper":
		
			compFunc.comparison("player_lose")

			#print(" You lose! So bad!")
			#gameVars.player_lives -= 1

		else:
			#print(" You win! Nice one Warrior!")
			#gameVars.computer_lives -= 1
			compFunc.comparison("player_won")

	if gameVars.player_lives == 0:
		winLose.winorlose("lose")

	if gameVars.computer_lives == 0:
		winLose.winorlose("won")
		

	#print("player_lives:", gameVars.player_lives)
	#print("computer_lives:", gameVars.computer_lives)

	# make the loop keep running by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True

	gameVars.player_choice = False