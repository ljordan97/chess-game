import leviChess as lc

game = lc.startGame()
#print(game.active)

while game.active:
	game.nextTurn()