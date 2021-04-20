import leviChess as lc

##initialization 

BOARD_OFFSET_X = 79
BOARD_OFFSET_Y = 79
SPRITE_SIZE = 79

#dictionary of every square coordinate, as strings. e.g. "e4"
#from black POV
board = {chr(72 - j) + str(i + 1):[(BOARD_OFFSET_X + (j * SPRITE_SIZE), BOARD_OFFSET_Y + (i * SPRITE_SIZE))] for i in range(8) for j in range(8)}
print(board)

#lc.init_graphics()
lc.pygame.init()
size = width, height = 768, 768 #screen size
screen = lc.pygame.display.set_mode(size) #create screen
lc.pygame.display.set_caption('Levi\'s Chess')
lc.pygame.mouse.set_visible(1)

#load board asset
background = lc.pygame.image.load("assets/chess_board.png")
background_rect = background.get_rect()

#render board
screen.blit(background, background_rect)

#store all pieces in list
pieces = []
#instantiate pieces, add to piece list
pieces.extend([lc.Piece("white", "pawn", chr(65 + num) + str(2), board) for num in range(8)])
pieces.extend([lc.Piece("black", "pawn", chr(65 + num) + str(7), board) for num in range(8)])
pieces.extend([lc.Piece("white", "rook", chr(65 + (num * 7)) + str(1), board) for num in range(2)])
pieces.extend([lc.Piece("black", "rook", chr(65 + (num * 7)) + str(8), board) for num in range(2)])
pieces.extend([lc.Piece("white", "knight", chr(65 + ((num * 5) + 1)) + str(1), board) for num in range(2)])
pieces.extend([lc.Piece("black", "knight", chr(65 + ((num * 5) + 1)) + str(8), board) for num in range(2)])
pieces.extend([lc.Piece("white", "bishop", chr(65 + ((num * 3) + 2)) + str(1), board) for num in range(2)])
pieces.extend([lc.Piece("black", "bishop", chr(65 + ((num * 3) + 2)) + str(8), board) for num in range(2)])
pieces.extend([lc.Piece("white", "queen", "D1", board)])
pieces.extend([lc.Piece("black", "queen", "D8", board)])
pieces.extend([lc.Piece("white", "king", "E1", board)])
pieces.extend([lc.Piece("black", "king", "E8", board)])

#white to move first
turn = 0
#true when a piece has been clicked already, removes need for nested loops
piece_selected = 0
#main loop
while 1:
	#render all sprites
	for piece in pieces:
		#piece.rect.inflate(50,50)
		screen.blit(piece.image, piece.rect)

	#update display
	lc.pygame.display.flip()

	#get updated event queue
	ev = lc.pygame.event.get()

	#select piece with a click, move the piece with the next click
	for event in ev:
		#if a piece is clicked and none are currently selected
		if event.type == lc.pygame.MOUSEBUTTONDOWN and piece_selected == 0:
			#get click position
			pos = lc.pygame.mouse.get_pos()
			# get a list of all sprites that are under the mouse cursor
			clicked_sprites = [s for s in pieces if s.rect.collidepoint(pos)]
			if clicked_sprites:
				#enlarge selected piece for emphasis
				clicked_sprites[0].image = lc.pygame.transform.scale(clicked_sprites[0].image, (72, 72))
				#next click will move the piece instead of selecting another sprite
				piece_selected = 1
			print("1st click selected ", clicked_sprites, piece_selected)

		#if a piece has been selected and needs to move
		elif event.type == lc.pygame.MOUSEBUTTONDOWN and piece_selected == 1:
			#get new click pos
			pos = lc.pygame.mouse.get_pos()
			print(pos)
			#update position of previously selected sprite
			#TO DO: RESOLVE NEAREST SQUARE POSITION BEFORE MOVING
				#also, remove the old sprite image
			clicked_sprites[0].rect.topleft = pos
			
			#let another piece get selected 
			piece_selected = 0
			print("second click", piece_selected)
			#erase list of clicked sprites
			clicked_sprites = []
			print("sprites selected after 2nd click ", clicked_sprites)

	#erase queue to make way for fresh clicks
	lc.pygame.event.clear()
	ev = lc.pygame.event.get()

	#end and toggle turn
	turn = turn ^ 1
		