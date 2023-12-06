from automatons.classes.dfa import DFA
from automatons.classes.nfa import NFA
from automatons.constructors.dfa_from_nfa import dfa_from_nfa
from automatons.constructors.nfa_from_regex import nfa_from_regex
from regex.nodes.regex_node import RegexNode


def minimal_full_dfa_from_regex(regex: RegexNode, terminal=None) -> DFA:
    nfa = nfa_from_regex(regex, terminal)
    return minimal_full_dfa_from_nfa(nfa)


def minimal_full_dfa_from_nfa(nfa: NFA) -> DFA:
    dfa = dfa_from_nfa(nfa)
    dfa.minimize()
    dfa.delete_unreachable_states()
    dfa.make_full()

    return dfa
