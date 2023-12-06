from automatons.constructors.mfdfa import \
    minimal_full_dfa_from_regex
from automatons.constructors.nfa_from_regex import nfa_from_regex
from regex.nodes.binary_node import BinaryNode, RegexOperations
from regex.nodes.leaf_node import LeafNode


def test_minimal_dfa_from_regex():
    a = LeafNode('a')
    b = LeafNode('b')
    c = LeafNode('c')
    ab = BinaryNode(a, b, RegexOperations.UNITE)
    abc = BinaryNode(ab, c, RegexOperations.UNITE)
    ac = BinaryNode(a, c, RegexOperations.CONCAT)
    ab_cl = BinaryNode(ab, None, RegexOperations.CLOSURE)

    nfa = nfa_from_regex(ab_cl, "ab_cl")
    print(f"NFA for {ab_cl}")
    nfa.print()
    print("\n")
    dfa = minimal_full_dfa_from_regex(ab_cl, str(ab_cl))
    print(f"DFA for {ab_cl}")
    dfa.print()

    ac_cl = BinaryNode(ac, None, RegexOperations.CLOSURE)
    ab_cl_plus_ac_cl = BinaryNode(ab_cl, ac_cl, RegexOperations.UNITE)
    ab_cl_plus_ac_cl_cl = BinaryNode(ab_cl_plus_ac_cl, None,
                                     RegexOperations.CLOSURE)

    print(ab_cl_plus_ac_cl_cl)
    dfa = minimal_full_dfa_from_regex(ab_cl_plus_ac_cl_cl,
                                      str(ab_cl_plus_ac_cl_cl))

    dfa.print()
