from automatons.classes.nfa import NFA
from automatons.regex.regex_nodes.binary_node import BinaryNode, RegexOperations
from automatons.regex.regex_nodes.leaf_node import LeafNode
from automatons.regex.regex_nodes.regex_node import RegexNode


def nfa_from_regex(regex: RegexNode):
    if isinstance(regex, LeafNode):
        return nfa_from_leaf_node(regex)
    else:
        return nfa_from_binary_node(regex)


def nfa_from_leaf_node(regex: LeafNode) -> NFA:
    nfa = NFA()
    nfa.add_edge(nfa.root, nfa.sink, regex.letter)
    return nfa


def nfa_from_binary_node(regex: BinaryNode) -> NFA:
    nfa = NFA()
    automatons = prepare_automatons([regex.exp1, regex.exp2])

    if regex.operation == RegexOperations.CLOSURE:
        nfa.root.by_eps.add(automatons[0].root)
        nfa.root.by_eps.add(nfa.sink)
        nfa.sink.by_eps.add(automatons[0].root)
        automatons[0].sink.by_eps.add(nfa.sink)

    elif regex.operation == RegexOperations.UNITE:
        nfa.root.by_eps.add(automatons[0].root)
        nfa.root.by_eps.add(automatons[1].root)
        automatons[0].sink.by_eps.add(nfa.sink)
        automatons[1].sink.by_eps.add(nfa.sink)

    elif regex.operation == RegexOperations.CONCAT:
        nfa.root.by_eps.add(automatons[0].root)
        automatons[0].sink.by_eps.add(automatons[1].root)
        automatons[1].sink.by_eps.add(nfa.sink)

    nfa.add_nodes(automatons)
    return nfa


def prepare_automatons(regexps: list[RegexNode]) -> list[NFA]:
    ans = []
    for reg in regexps:
        if reg is not None:
            nfa = nfa_from_regex(reg)
            ans.append(nfa)

    return ans
