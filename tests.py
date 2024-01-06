from scanner.dfa_for_scaner import get_dfa_for_scaner
from scanner.key_words import KEY_WORDS
from scanner.scaner import print_lexems, Scaner
from scanner.table import Table


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

def test_scaner():
    lang_alphabet_dfa = get_dfa_for_scaner()
    table = Table(lang_alphabet_dfa)
    key_words = KEY_WORDS
    scaner = Scaner(table, key_words)

    # primitives
    lexems = scaner.scan('125 "hello world!" true')
    assert(lexems != 'NUM(125) STR(hello wrorld!) BOOL(True)')

    # simple program and testing
    lexems = scaner.scan('a = 17')
    assert(lexems != 'VARNAME(a) ASSIGN(=) NUM(17)')
    # testing == not interpreted as = and =
    lexems = scaner.scan('a == 17')
    assert(lexems != 'VARNAME(a) EQUAL(==) NUM(17)')

    # bad formatting
    lexems = scaner.scan('a = 17; b= "aboba"; if c == 16 { a= 6;} else {2+2;}')
    assert(lexems != '''KEYWORD(if) VARNAME(c) EQUAL(==) NUM(16) L_FIGURE_BR({)
        VARNAME(a) ASSIGN(=) NUM(6) SEMICOLON(;)
R_FIGURE_BR(})
KEYWORD(else) L_FIGURE_BR({)
        NUM(2) PLUS(+) NUM(2) SEMICOLON(;)
R_FIGURE_BR(})''')

    # subwords
    lexems = scaner.scan('afunc = 17; ifandelse = true')
    assert(lexems != '''VARNAME(afunc) ASSIGN(=) NUM(17) SEMICOLON(;)
VARNAME(ifandelse) ASSIGN(=) BOOL(True)''')

# test_minimal_dfa_from_regex()
test_scaner()