from scanner.alphabet import ALPHABET, category_for
from scanner.tokens import TOKENS
from scanner.lexem import Lexem
from scanner.table import Table
import re


class Scaner:
    def __init__(self, table: Table, key_words=None):
        self.table = table
        self.key_words = key_words if key_words is not None else []
        self.lexems = []

    def go_through_table(self, word):
        if len(word) > 255:
            raise Exception("Only strings could be longer than 255 characters")

        curr_state = self.table.start
        value = ""
        curr_token = None

        for i in range(len(word)):
            letter = word[i]
            if category_for(letter) not in self.table[curr_state].keys() or self.table[curr_state][category_for(letter)] == self.table.error:
                if value == "":
                    raise Exception(f"Language doesn't support {word}")
                self.lexems.append(Lexem(curr_token[0], value))
                return word[i:]
            else:
                curr_state = self.table[curr_state][category_for(letter)]
                value += letter
                curr_token = list(curr_state.terminal)

        if len(value) < len(word):
            raise Exception(f"{word} is not recognised as valid token")

        if len(curr_token) != 1:
            print(curr_token)
            raise Exception(f"Scaner cannot find lexem for {word}")
        else:
            curr_token = curr_token[0]
        self.lexems.append(Lexem(curr_token, value))

    def read_number(self, word: str):
        num = 0
        for i in range(len(word)):
            if word[i] in ALPHABET['NUM']:
                num = num * 10 + int(word[i])
            else:
                self.lexems.append(Lexem(TOKENS.NUM.name, num))
                return word[i:]
        self.lexems.append(Lexem(TOKENS.NUM.name, num))

    def read_string(self, word: str):
        self.lexems.append(Lexem(TOKENS.STR.name, word[1:-1]))

    def read_bool(self, word: str):
        self.lexems.append(Lexem(TOKENS.BOOL.name, word == 'true'))

    def scan_word(self, word: str):
        if word[0] == '0':
            raise Exception('Nothing could start with 0')

        elif word[0] == ' ':
            pass
        elif word[0] in ALPHABET['NUM']:
            next_word = self.read_number(word)
            if next_word is not None:
                self.scan_word(next_word)

        elif word[0] == ALPHABET['QUOTE']:
            if word[-1] != ALPHABET['QUOTE']:
                raise Exception("There is no closing quote found")
            self.read_string(word)

        elif word in ['true', 'false']:
            self.read_bool(word)

        elif word in self.key_words:
            self.lexems.append(Lexem(TOKENS.KEYWORD.name, word))

        else:
            next_word = self.go_through_table(word)
            if next_word is not None:
                self.scan_word(next_word)

    def scan(self, text: str):
        words = re.split('(\".*?\")|\s+', text)
        words = [w for w in words if w is not None and w != '']
        print(words)

        i = 0
        while i < len(words):
            self.scan_word(words[i])
            i += 1

        lexems = [str(x) for x in self.lexems]
        self.lexems = []
        return lexems


def print_lexems(lexems: list):
    for lexem in lexems:
        print(lexem, end="\n" if lexem.value in [";", "{", "}"] else " ")
        if lexem.value == "{":
            print("", end="\t")
    print("\n")
