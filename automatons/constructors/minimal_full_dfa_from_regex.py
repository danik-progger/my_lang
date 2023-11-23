from automatons.classes.dfa import DFA
from automatons.constructors.dfa_from_nfa import dfa_from_nfa
from automatons.constructors.nfa_from_regex import nfa_from_regex
from automatons.regex.regex_nodes.regex_node import RegexNode


def minimal_full_dfa_from_regex(regex: RegexNode) -> DFA:
    nfa = nfa_from_regex(regex)
    nfa.delete_epsilon_transitions()
    dfa = dfa_from_nfa(nfa)
    dfa.minimize()
    dfa.make_full()

    return dfa
