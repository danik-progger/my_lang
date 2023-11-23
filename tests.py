from automatons.constructors.minimal_full_dfa_from_regex import \
    minimal_full_dfa_from_regex
from automatons.regex.regex_nodes.binary_node import BinaryNode, RegexOperations
from automatons.regex.regex_nodes.leaf_node import LeafNode


def test_minimal_dfa_from_regex():
    a = LeafNode('a')
    b = LeafNode('b')
    c = LeafNode('c')
    ab = BinaryNode(a, b, RegexOperations.CONCAT)
    ac = BinaryNode(a, c, RegexOperations.CONCAT)
    ab = BinaryNode(ab, None, RegexOperations.CLOSURE)
    ac = BinaryNode(ac, None, RegexOperations.CLOSURE)
    ab = BinaryNode(ab, ac, RegexOperations.UNITE)
    ab = BinaryNode(ab, None, RegexOperations.CLOSURE)

    print(ab)
    dfa = minimal_full_dfa_from_regex(ab)

    print("states:", len(dfa.states))
    for state in dfa.states:
        print(state)
        print(state.to)
        print("\n")


def test_scaner():
    pass
