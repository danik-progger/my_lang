from automatons.classes.nfa import NFA
from automatons.constructors.nfa_operations import closure_automaton, concat_automatons, unite_automatons
from regex.nodes.binary_node import BinaryNode, RegexOperations
from regex.nodes.leaf_node import LeafNode
from regex.nodes.regex_node import RegexNode


def nfa_from_regex(regex: RegexNode, terminal=None):
    if isinstance(regex, LeafNode):
        nfa = nfa_from_leaf_node(regex)
    else:
        nfa = nfa_from_binary_node(regex)
    if terminal is not None:
        nfa.sink.make_terminal(terminal)

    return nfa


def nfa_from_leaf_node(regex: LeafNode) -> NFA:
    nfa = NFA()
    nfa.add_edge(nfa.root, nfa.sink, regex.letter)
    return nfa


def nfa_from_binary_node(regex: BinaryNode) -> NFA:
    automatons = automatons_from_regexps([regex.exp1, regex.exp2])

    if regex.operation == RegexOperations.CLOSURE:
        return closure_automaton(automatons[0])

    elif regex.operation == RegexOperations.UNITE:
        return unite_automatons(automatons)

    elif regex.operation == RegexOperations.CONCAT:
        return concat_automatons(automatons)


def automatons_from_regexps(regexps: list[RegexNode]) -> list[NFA]:
    ans = []
    for reg in regexps:
        if reg is not None:
            nfa = nfa_from_regex(reg)
            ans.append(nfa)

    return ans
