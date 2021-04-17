#the alphabetic coordinate is represented numerically for processing
#pieces are numbered kingside lowest
class Piece:
	def __init__(self, color, piece, num=0):
		self.num = num #id for multiple
		self.captured = 0 #if 1, piece has been captured
		self.color = color #string, "white" or "black"
		self.piece = piece #string. e.g. "pawn"

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

		self.proper_coordinate = [chr(65 + self.location[1]), self.location[0]]

		print("Created " + self.color + " " + self.piece + " at " + str(self.proper_coordinate[0]) + str(self.proper_coordinate[1]))

	def __repr__(self):
		if self.piece != "queen" or self.piece != "king":
			return self.color + self.piece + str(self.num)
		else:
			return self.color + self.piece

def initPieces():
	white_pawns = [Piece("white", "pawn", num) for num in range(8)]
	black_pawns = [Piece("black", "pawn", num) for num in range(8)]
	white_rooks = [Piece("white", "rook", num) for num in range(2)]
	black_rooks = [Piece("black", "rook", num) for num in range(2)]
	white_knights = [Piece("white", "knight", num) for num in range(2)]
	black_knights = [Piece("black", "knight", num) for num in range(2)]
	white_bishops = [Piece("white", "bishop", num) for num in range(2)]
	black_bishops = [Piece("black", "bishop", num) for num in range(2)]
	white_king = Piece("white", "king")
	black_king = Piece("black", "king")
	white_queen = Piece("white", "queen")
	black_queen = Piece("black", "queen")
	
initPieces()