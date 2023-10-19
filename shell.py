from textvid import Lexer

while True:
    text = input("basic > ")
    print(Lexer(text).make_tokens())