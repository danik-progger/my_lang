from scanner.dfa_for_scaner import get_dfa_for_scaner
from scanner.key_words import KEY_WORDS
from scanner.scaner import print_lexems, Scaner
from scanner.table import Table


def test_scaner():
    lang_alphabet_dfa = get_dfa_for_scaner()
    table = Table(lang_alphabet_dfa)
    key_words = KEY_WORDS
    scaner = Scaner(table, key_words)

    # primitives
    lexems = scaner.scan('125 "hello world!" true')
    print_lexems(lexems)

    # simple program and testing
    lexems = scaner.scan('a = 17')
    print_lexems(lexems)
    # testing == not interpreted as = and =
    lexems = scaner.scan('a == 17')
    print_lexems(lexems)

    # bad formatting
    lexems = scaner.scan('a = 17; b= "aboba"; if c == 16 { a= 6;} else {2+2;}')
    print_lexems(lexems)

    # subwords
    lexems = scaner.scan('afunc = 17; ifandelse = true')
    print_lexems(lexems)

