import re
from enum import Enum


class Token(Enum):
    OPENBRACE = 1
    CLOSEBRACE = 2
    EQUALS = 3
    TEXT = 11
    NUMBER = 12
    NAMESPACE = 13


class DataToken:
    def __init__(self, token_type, data=""):
        self.token_type = token_type
        self.data = data

    def __repr__(self):
        return self.token_type.name + ":" + self.data


class Lexer:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.data = ""
        self.tokens = []
        self.curr_token = 0

        self.lex_input()

    def lex_input(self):
        with open(self.input_file, "r", encoding="latin-1") as infile:
            self.data = infile.read()

        basic_regex = "{|}|-?\d+(\.\d+)?\b|\
        namespace|=|#.*\\n?|[öÖåÅäÄüÜíÍéÉàÀA-ZòÒa-z'-\.\d_:\w]+|\"['\wòÒöÖåÅäÄüÜíÍéÉàÀA-Za-z-._ ]+\""

        match_dict = {
            "{": Token.OPENBRACE,
            "}": Token.CLOSEBRACE,
            "=": Token.EQUALS,
            "namespace": Token.NAMESPACE,
        }

        for match in re.finditer(basic_regex, self.data):
            if match.group() in match_dict:
                token = DataToken(match_dict.get(match.group()))
                self.tokens.append(token)
            elif len(match.group()) == 0:
                continue
            elif match.group()[0] == "#":
                continue
            elif match.group()[0].isdigit():
                self.tokens.append(DataToken(Token.NUMBER, match.group()))
            else:
                self.tokens.append(DataToken(Token.TEXT, match.group()))

    def get_token(self):
        token = self.tokens[self.curr_token]
        self.curr_token += 1
        return token

    def peek_token(self):
        return self.tokens[self.curr_token]

    def has_more_tokens(self):
        return self.curr_token < len(self.tokens)
