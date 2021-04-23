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

#create container for sprites
allsprites = lc.pygame.sprite.RenderPlain(pieces)

#init gameclock to spare cpu usage
clock = lc.pygame.time.Clock()

#main loop
while 1:
	clock.tick(60)

	#this will restrict moveable pieces based on turn
	if turn == 0:
		to_move = "white"
	elif turn == 1:
		to_move = "black"

	#render board
	screen.blit(background, background_rect)

	#draw all sprites (TODO: ...that aren't captured)
	allsprites.draw(screen)

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
				#if the piece has been clicked and it is the right team's turn
				if clicked_sprites[0].color == to_move:

					#enlarge selected piece for emphasis
					clicked_sprites[0].image = lc.pygame.transform.smoothscale(\
						clicked_sprites[0].image, (80, 80))

					#recenter enlarged sprite
					clicked_sprites[0].rect = clicked_sprites[0].rect.move(\
						(-12, -12))

					#next click will move the piece instead of selecting another sprite
					piece_selected = 1
					print(clicked_sprites[0].image)

				#if piece selected out of turn
				elif clicked_sprites[0].color != to_move:	
					print("wrong turn")
					


			print("1st click selected ", clicked_sprites, piece_selected)

		#if a piece has been selected and needs to move
		elif event.type == lc.pygame.MOUSEBUTTONDOWN and piece_selected == 1:
			#reset piece selection for next click
			piece_selected = 0

			#get new click pos
			pos2 = lc.pygame.mouse.get_pos()
			print("pos2", pos2)
			#check if another piece was clicked on, if it's the same color, 
			#select it instead of moving (unless king is castling)
			# get a list of all sprites that are under the mouse cursor
			new_clicked_sprites = [p for p in pieces if p.rect.collidepoint(pos2)]
			print(new_clicked_sprites)
			
			#logic for castling must be handled separately
			# if ((clicked_sprites[0].rank == "king" and new_clicked_sprites[0].rank == "rook")\
			# and (clicked_sprites[0].color == to_move and new_clicked_sprites[0].color == to_move):
			# 	print("castle attempted, no logic yet")
			
			#if another piece is clicked on (instead of open square)
			if new_clicked_sprites:

				#if the player tries to move to a square they already occupy
				if new_clicked_sprites[0].color == to_move:
					#just select that new piece
					#enlarge selected piece for emphasis
					new_clicked_sprites[0].image = lc.pygame.transform.smoothscale(\
					new_clicked_sprites[0].image, (80, 80))

					#unenlarge the old piece
					clicked_sprites[0].image = lc.pygame.transform.smoothscale(\
					clicked_sprites[0].image, (60, 60))

					#recenter enlarged sprite
					new_clicked_sprites[0].rect = new_clicked_sprites[0].rect.move(\
						(-12, -12))

					#next click will move the piece instead of selecting another sprite
					piece_selected = 1
					print(new_clicked_sprites[0].image)
			
			#if an open square is clicked
			else:
				#un-enlarge piece for placement
				clicked_sprites[0].image, clicked_sprites[0].rect = lc.load_image(\
					clicked_sprites[0].color + "_" + clicked_sprites[0].rank + ".png", -1)

				#get the square that was clicked on 
				new_square = resolveSquare(pos2)
				print(new_square)
				#pull the corresponding coordinate from board dict, render piece there
				clicked_sprites[0].rect.topleft = board[new_square][0]
				
				#let another piece get selected 
				print("second click", piece_selected)

				#erase list of clicked sprites
				clicked_sprites = []
				print("sprites selected after 2nd click ", clicked_sprites)

				#change turns
				turn = turn ^ 1

	#erase queue to make way for fresh clicks
	lc.pygame.event.clear()
	
	def resolveSquare(mouse_click):
		selectedRow = lc.math.floor(mouse_click[1] / 79)
		selectedCol = lc.math.floor(mouse_click[0] / 79) - 1
		#convert column to character
		selectedCol = chr(72 -selectedCol)
		new_square = selectedCol + str(selectedRow)
		#return square
		print(mouse_click)
		print(new_square)
		return new_square