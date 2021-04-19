import os, sys, pygame
from pygame.locals import *

#white_pawn = Piece("white", "pawn", board, "G1")
class Piece(pygame.sprite.Sprite):
	
	def __init__(self, color, rank, starting_square, board):
		#to allow pygame sprite methods to be used
		pygame.sprite.Sprite.__init__(self)

		self.board = board

		#attributes for identification
		self.color = color
		self.rank = rank
		self.current_square = starting_square

		#attributes for graphics
		self.image, self.rect = load_image(self.color + "_" + self.rank + ".png", -1)
		#move rect to proper spot
		self.rect.topleft = self.board[self.current_square][0]
		print("Created " + self.color + " " + self.rank + " at " + starting_square)

		#add piece to board dict
		square_data = self.board[self.current_square]
		square_data.append(self)

def init_graphics():
	pygame.init()
	size = width, height = 768, 768 #screen size
	screen = pygame.display.set_mode(size) #create screen
	pygame.display.set_caption('Levi\'s Chess')
	pygame.mouse.set_visible(0)

	#load board asset
	background = pygame.image.load("assets/chess_board.png")
	background_rect = background.get_rect()

	#render board
	screen.blit(background, background_rect)
	pygame.display.flip()

def init_pieces():
	white_pawns = [Piece("white", "pawn", chr(65 + num) + str(2)) for num in range(8)]
	black_pawns = [Piece("black", "pawn", chr(65 + num) + str(7)) for num in range(8)]
	# white_rooks = [Piece("white", "rook", num) for num in range(2)]
	# black_rooks = [Piece("black", "rook", num) for num in range(2)]
	# white_knights = [Piece("white", "knight", num) for num in range(2)]
	# black_knights = [Piece("black", "knight", num) for num in range(2)]
	# white_bishops = [Piece("white", "bishop", num) for num in range(2)]
	# black_bishops = [Piece("black", "bishop", num) for num in range(2)]
	# white_king = [Piece("white", "king")]
	# black_king = [Piece("black", "king")]
	# white_queen = [Piece("white", "queen")]
	# black_queen = [Piece("black", "queen")]

def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    # image = image.convert()
    # if colorkey is not None:
    #     if colorkey is -1:
    #         colorkey = image.get_at((0, 0))
    #     image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def next_turn():
	pass