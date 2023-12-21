import alphabet
from regex.regex_nodes.binary_node import BinaryNode, RegexOperations
from regex.regex_nodes.leaf_node import LeafNode


def get_var_name_regex() -> BinaryNode:
    letters = LeafNode()
    for letter in alphabet.LETTERS:
        letters = BinaryNode(letters, LeafNode(letter), RegexOperations.UNITE)

    other = LeafNode()
    for letter in alphabet.NUMBERS + alphabet.UNDERSCORE:
        other = BinaryNode(other, LeafNode(letter), RegexOperations.UNITE)
    other = BinaryNode(other, letters, RegexOperations.UNITE)
    other = BinaryNode(other, None, RegexOperations.CLOSURE)

    regex = BinaryNode(letters, other, RegexOperations.UNITE)
    return regex


TOKENS_REGEXPS = {
    'NUM': LeafNode(),
    'STR': LeafNode(),
    'BOOL': LeafNode(),
    'VARNAME': get_var_name_regex(),
    'L_ROUND_BR': LeafNode(alphabet.L_ROUND_BR),
    'R_ROUND_BR': LeafNode(alphabet.R_ROUND_BR),
    'L_FIGURE_BR': LeafNode(alphabet.L_FIGURE_BR),
    'R_FIGURE_BR': LeafNode(alphabet.R_FIGURE_BR),
    'QUOTE': LeafNode(alphabet.QUOTE),
    'SEMICOLON': LeafNode(alphabet.SEMICOLON),
    'DOT': LeafNode(alphabet.DOT),
}
