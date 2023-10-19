###########
# CONSTANTS
###########
DIGITS = "0123456789"

###########
# ERRORS
###########
class Error:
	def __init__(self) -> None:
		pass

###########
# TOKENS
###########
TT_INT		= 'TT_INT'
TT_FLOAT	= 'TT_FLOAT'
TT_PLUS		= 'TT_PLUS'
TT_MINUS	= 'TT_MINUS'
TT_MUL		= 'TT_MUL'
TT_DIV		= 'TT_DIV'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'

class Token:
	def __init__(self, _type, value):
		self.type = _type
		self.value = value

	def __repr__(self) -> str:
		if self.value: return f"{self.type}:{self.value}"
		return f"{self.type}"
    
class Lexer:
	def __init__(self, text) -> None:
		self.text = text
		self.pos = -1
		self.current_char = None
		self.advance()
	
	def advance(self):
		self.pos += 1
		self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
	
	def make_tokens(self):
		tokens = []

		while self.current_char != None:
			if self.current_char in ' \t':
				self.advance()
				continue
			if self.current_char in DIGITS:
				tokens.append(self.make_number())
			if self.current_char == '+':
				tokens.append(Token(TT_PLUS))
				self.advance()
				continue
			if self.current_char == '-':
				tokens.append(Token(TT_MINUS))
				self.advance()
				continue
			if self.current_char == '*':
				tokens.append(Token(TT_MUL))
				self.advance()
				continue
			if self.current_char == '/':
				tokens.append(Token(TT_DIV))
				self.advance()
				continue
			if self.current_char == '(':
				tokens.append(Token(TT_LPAREN))
				self.advance()
				continue
			if self.current_char == ')':
				tokens.append(Token(TT_RPAREN))
				self.advance()
				continue

		return tokens

	def make_number(self):
		num_str = ""
		dot_count = 0

		while self.current_char != None and self.current_char in DIGITS + ".":
			if self.current_char == ".":
				if dot_count == 1: break
				dot_count += 1
				num_str += "."
			else:
				num_str += self.current_char
		
		if dot_count == 0:
			return Token(TT_INT, int(num_str))
		return Token(TT_FLOAT, float(num_str))
		