from gameComponents import gameVars

def comparison(status):
	
	if status == "player_won":
		print(" You ARE A REAL KICKASS! Nice one Warrior!")

		gameVars.computer_lives -= 1
	
	elif status == "player_lose":
		print(" Damn Warrior, not this time...")

		gameVars.player_lives -= 1

	elif status == "game_tie":
		print(" Tie! No one wins! Play again!")