import sys, pygame

class Game:
	def __init__(self, white_pieces, black_pieces):
		self.turn = 0
		self.active = 1 #game is active until checkmate
		self.white_pieces = white_pieces
		self.black_pieces = black_pieces
		print("Starting a new game...")

		#init graphics
		pygame.init()
		size = width, height = 768, 768
		screen = pygame.display.set_mode(size)

		board = pygame.image.load("assets/chess_board.png")
		board_rect = board.get_rect()

		screen.blit(board, board_rect)
		pygame.display.flip()

		for piece_type in white_pieces.values():
			print(piece_type)
			for piece in piece_type:
				print(piece.graphic)
				piece.graphic = pygame.image.load("assets/" + piece.color + "_" + piece.piece + ".png")
				print(piece.graphic)
				piece.graphic_rect = piece.graphic.get_rect()
				print(piece.location)
				piece.graphic_rect.move(5, 5)
				screen.blit(piece.graphic, board_rect)

				print("drawing " + piece.color + " " + piece.piece)
				pygame.display.flip()

	def nextTurn(self):
		print("i got here")
		if self.turn == 0:
			self.next_move = input("White to move: ")
		elif self.turn == 1:
			self.next_move = input("Black to move: ")
		self.turn = self.turn ^ 1 #toggle boolean

		#parse move

			#id piece to move
			#get new location
			#check legality of move

#the alphabetic coordinate is represented numerically for processing
#pieces are numbered kingside lowest
class Piece:
	def __init__(self, color, piece, num=0):
		self.num = num #id for multiple
		self.captured = 0 #if 1, piece has been captured
		self.color = color #string, "white" or "black"
		self.piece = piece #string. e.g. "pawn"
		self.graphic = 0 #will store pygame data of piece image
		self.graphic_rect = 0 #will store pygame data of piece loc
		#get row to assign position to
		if self.color == "white":
			starting_pawn_row = 1
			starting_main_row = 0
		else:
			starting_pawn_row = 6
			starting_main_row = 7

		#assign starting position based on piece
		if self.piece == "pawn":
			self.location = [starting_pawn_row, num]
		elif self.piece == "rook":
			self.location = [starting_main_row, 0 + 7 * num]
		elif self.piece == "knight":
			self.location = [starting_main_row, 1 + 5 * num]
		elif self.piece == "bishop":
			self.location = [starting_main_row, 2 + 3 * num]
		elif self.piece == "king":
			self.location = [starting_main_row, 3]
		elif self.piece == "queen":
			self.location = [starting_main_row, 4]

		self.proper_coordinate = [chr(65 + self.location[1]), self.location[0] + 1]

		print("Created " + self.color + " " + self.piece + " at " + str(self.proper_coordinate[0]) + str(self.proper_coordinate[1]))

	def __repr__(self):
		if self.piece != "queen" or self.piece != "king":
			return self.color + self.piece + str(self.num)
		else:
			return self.color + self.piece

def initPieces():
	#create object for each piece
	white_pawns = [Piece("white", "pawn", num) for num in range(8)]
	black_pawns = [Piece("black", "pawn", num) for num in range(8)]
	white_rooks = [Piece("white", "rook", num) for num in range(2)]
	black_rooks = [Piece("black", "rook", num) for num in range(2)]
	white_knights = [Piece("white", "knight", num) for num in range(2)]
	black_knights = [Piece("black", "knight", num) for num in range(2)]
	white_bishops = [Piece("white", "bishop", num) for num in range(2)]
	black_bishops = [Piece("black", "bishop", num) for num in range(2)]
	white_king = [Piece("white", "king")]
	black_king = [Piece("black", "king")]
	white_queen = [Piece("white", "queen")]
	black_queen = [Piece("black", "queen")]

	#organize pieces into dictionaries, to be used by Game class
	white_pieces = {
	"pawns": white_pawns,
	"rooks": white_rooks,
	"knights": white_knights,
	"bishops": white_bishops,
	"queen": white_queen,
	"king": white_king
	}

	black_pieces = {
	"pawns": black_pawns,
	"rooks": black_rooks,
	"knights": black_knights,
	"bishops": black_bishops,
	"queen": black_queen,
	"king": black_king
	}

	return white_pieces, black_pieces

def startGame():
	print("This chess game is played using Portable Game Notation to describe your move.")
	pieces = initPieces()
	game = Game(pieces[0], pieces[1])
	return game
	
