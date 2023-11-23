from automatons.classes.dfa import DFA
from automatons.classes.nfa import NFA
from automatons.nodes.dfa_node import DFA_Node
from automatons.nodes.nfa_node import NFA_Node


def get_move(source: set[NFA_Node], letter: str) -> set[NFA_Node]:
    move = set()
    for node in source:
        if letter in node.to.keys():
            for neighbour in node.to[letter]:
                move.add(neighbour)

    return move


def dfa_from_nfa(nfa: NFA) -> DFA:
    dfa_nodes = []
    transitions = dict()

    queue = [frozenset([nfa.root])]
    dfa_nodes.append(frozenset([nfa.root]))
    used = set()

    while len(queue) > 0:
        curr_state = queue.pop(0)

        letters = set()
        for vert in curr_state:
            for letter in vert.to.keys():
                letters.add(letter)

        for letter in letters:
            next_state = frozenset(get_move(curr_state, letter))
            if curr_state not in transitions.keys():
                transitions[curr_state] = dict()
            transitions[curr_state][letter] = next_state

            if next_state not in used:
                queue.append(next_state)
                used.add(next_state)
                dfa_nodes.append(next_state)

    dfa = DFA()
    equivalent = dict()
    for node in dfa_nodes:
        if nfa.root in node:
            dfa.root = DFA_Node(node)
            equivalent[node] = dfa.root
        else:
            new_node = DFA_Node(node)
            dfa.states.add(new_node)
            equivalent[node] = new_node

    for source, letter_transitions in transitions.items():
        for letter, target in letter_transitions.items():
            dfa.add_edge(equivalent[source], equivalent[transitions[source][letter]], letter)

    dfa.delete_unreachable_states()
    dfa.states.add(dfa.trash)

    return dfa

