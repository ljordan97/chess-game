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
lc.pygame.mouse.set_visible(0)

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

#render all sprites
for piece in pieces:
	piece.rect.inflate(50,50)
	screen.blit(piece.image, piece.rect)

#main loop
while 1:
	lc.pygame.display.flip()