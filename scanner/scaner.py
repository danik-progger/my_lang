from automatons.classes.dfa import DFA
from nodes.KeyWord import KeyWord
from nodes.expressions.leaf_expressions import LeafExpression
from nodes.expressions.leaf_expressions.bool import Bool
from nodes.expressions.leaf_expressions.number import Number
from nodes.expressions.leaf_expressions.str import String
from scanner.alphabet import QUOTE, SPEC_SYMBOLS, NUMBERS


class Scaner:
    def __init__(self, dfa: DFA, key_words=None):
        self.dfa = dfa
        self.key_words = key_words if key_words is not None else []
        self.tokens = []

    def go_through_dfa(self, word):
        if len(word) > 255:
            raise Exception("Only strings could be longer than 255 characters")

        curr_node = self.dfa.root
        value = ""
        curr_token = None

        for letter in word:
            if curr_node != self.dfa.trash:
                value += letter
                curr_token = list(curr_node.terminal)[0] \
                    if len(curr_node.terminal) > 0 else curr_token
                curr_node = curr_node.to[letter]

        if len(value) < len(word):
            raise Exception(f"{word} is not recognised as valid token")

        if len(curr_token) != 1:
            raise Exception(f"Compiler cannot choose token for {word}")

        self.tokens.append(curr_token(value))

    def read_number(self, word: str):
        num = 0
        if word[0] == 0:
            raise Exception("Number cannot start with 0")
        for letter in word:
            if letter in NUMBERS:
                num = num * 10 + int(letter)
            else:
                raise Exception(f"{word} is not number")

        self.tokens.append(Number(num))

    def read_string(self, word: str):
        next_quote_index = word.index(QUOTE)
        if next_quote_index < len(word) - 1:
            raise Exception("String cannot content quote")

        self.tokens.append(String(word[1:-1]))

    def read_bool(self, word: str):
        token = Bool(bool(word))
        self.tokens.append(token)

    def scan(self, text: str):
        for ch in text:
            if ch not in SPEC_SYMBOLS:
                if ch != QUOTE:
                    text.replace(f"{ch}", f" {ch} ")

        words = text.split()
        for i in range(len(words)):
            if words[i][0] == '0':
                raise Exception('nothing could start with 0')

            elif words[i][0] in NUMBERS:
                self.read_number(words[i])

            elif words[i][0] == QUOTE:
                i = self.read_string(words[i])

            elif words[i] in ['true', 'false']:
                self.read_bool(words[i])

            elif words[i] in self.key_words:
                self.tokens.append(KeyWord(words[i]))

            else:
                self.go_through_dfa(words[i])

    def print_tokens(self):
        for token in self.tokens:
            print(token, end="")
            if isinstance(token, LeafExpression):
                if token.value in [";", "{", "}"]:
                    print("\n")
            else:
                print(" ")
