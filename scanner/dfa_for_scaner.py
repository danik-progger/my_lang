from automatons.classes.dfa import DFA
from regex.nodes.binary_node import BinaryNode, RegexOperations
from regex.nodes.leaf_node import LeafNode
from automatons.constructors.nfa_from_regex import nfa_from_regex
from automatons.constructors.nfa_operations import unite_automatons
from automatons.constructors.mfdfa import minimal_full_dfa_from_nfa
from scanner.tokens import TOKENS
from scanner.alphabet import ALPHABET


def get_var_name_regex() -> BinaryNode:
    letters = LeafNode()
    for letter in ALPHABET['STR']:
        letters = BinaryNode(letters, LeafNode(letter), RegexOperations.UNITE)

    # other = LeafNode()
    # for letter in ALPHABET['NUM.value + ALPHABET['UNDERSCORE.value:
    #     other = BinaryNode(other, LeafNode(letter), RegexOperations.UNITE)
    # other = BinaryNode(other, letters, RegexOperations.UNITE)
    regex = BinaryNode(letters, None, RegexOperations.CLOSURE)
    regex = BinaryNode(letters, regex, RegexOperations.CONCAT)

    # regex = BinaryNode(letters, other, RegexOperations.UNITE)
    return regex


TOKENS_REGEXPS = {
    'VARNAME': get_var_name_regex(),
    'L_ROUND_BR': LeafNode(ALPHABET['L_ROUND_BR']),
    'R_ROUND_BR': LeafNode(ALPHABET['R_ROUND_BR']),
    'L_FIGURE_BR': LeafNode(ALPHABET['L_FIGURE_BR']),
    'R_FIGURE_BR': LeafNode(ALPHABET['R_FIGURE_BR']),
    'QUOTE': LeafNode(ALPHABET['QUOTE']),
    'SEMICOLON': LeafNode(ALPHABET['SEMICOLON']),
    'DOT': LeafNode(ALPHABET['DOT']),
    'EQUAL': BinaryNode(LeafNode(ALPHABET['ASSIGN']), LeafNode(ALPHABET['ASSIGN']), RegexOperations.CONCAT),
    'ASSIGN': LeafNode(ALPHABET['ASSIGN']),
    'PLUS': LeafNode(ALPHABET['PLUS']),
    'MINUS': LeafNode(ALPHABET['MINUS']),
    'STAR': LeafNode(ALPHABET['STAR']),
    'SLASH': LeafNode(ALPHABET['SLASH']),
    'NUM': None,
    'STR': None,
    'BOOL': None,
    'KEYWORD': None
}


def get_dfa_for_scaner() -> DFA:
    automatons = []
    for token, reg in TOKENS_REGEXPS.items():
        if reg is not None:
            nfa = nfa_from_regex(reg)
            nfa.sink.make_terminal(token)
            # print(token, TOKENS[token])
            automatons.append(nfa)

    final_nfa = unite_automatons(automatons)
    final_dfa = minimal_full_dfa_from_nfa(final_nfa)
    return final_dfa
