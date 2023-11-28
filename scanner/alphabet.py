from enum import Enum

ALPHABET = {
    'STR': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'NUM': '0123456789',
    'L_ROUND_BR': '(',
    'R_ROUND_BR': ')',
    'L_FIGURE_BR': '{',
    'R_FIGURE_BR': '}',
    'QUOTE': '"',
    'SEMICOLON': ';',
    'DOT': '.',
    'PLUS': '+',
    'MINUS': '-',
    'STAR': '*',
    'SLASH': '/',
    'UNDERSCORE': '_',
    'ASSIGN': '=',
    'EQUAL': '==',
}

SPEC_SYMBOLS = ['L_ROUND_BR', 'R_ROUND_BR', 'L_FIGURE_BR', 'R_FIGURE_BR',
                'ASSIGN', 'EQUAL', 'SEMICOLON', 'DOT', 'STAR', 'SLASH',
                'PLUS', 'MINUS']


def category_for(letter: str):
    for category, token in ALPHABET.items():
        if letter in token:
            return category
