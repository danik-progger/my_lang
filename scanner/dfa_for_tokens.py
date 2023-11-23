from automatons.classes.dfa import DFA
from automatons.constructors.minimal_full_dfa_from_regex import \
    minimal_full_dfa_from_regex
from regex.regex_nodes.binary_node import BinaryNode, RegexOperations
from regex.regex_nodes.leaf_node import LeafNode
from scanner.token_regexps import TOKENS_REGEXPS

TOKENS = [
    "L_ROUND_BR",
    "R_ROUND_BR",
    "L_FIGURE_BR",
    "R_FIGURE_BR",
    "QUOTE",
    "SEMICOLON",
    "DOT",
    "UNDERSCORE",
    "VARNAME"
]


def get_dfa_for_tokens() -> DFA:
    final_mega_regex = LeafNode()
    for token in TOKENS:
        final_mega_regex = BinaryNode(final_mega_regex, TOKENS_REGEXPS[token],
                                      RegexOperations.UNITE)

    mdfa = minimal_full_dfa_from_regex(final_mega_regex)
    return mdfa
