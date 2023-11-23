from automatons.classes.automaton import Automaton
from automatons.nodes.dfa_node import DFA_Node


class DFA(Automaton):
    def __init__(self, alphabet=None):
        super().__init__()
        self.root = DFA_Node()
        self.trash = DFA_Node()
        self.states.add(self.root)
        self.states.add(self.trash)

    def add_edge(self, source: DFA_Node, target: DFA_Node, letter: str):
        self.states.add(source)
        self.states.add(target)
        self.alphabet.add(letter)

        source.to[letter] = target

    def delete_unreachable_states(self):
        queue = [self.root]
        used = set()

        while len(queue) > 0:
            curr = queue.pop(0)

            for letter, state in curr.to.items():
                if state not in used:
                    queue.append(state)
                    used.add(state)

        for state in self.states - used:
            self.states.remove(state)

    def make_full(self):
        for state in self.states:
            for letter in self.alphabet:
                if letter not in state.to.keys():
                    self.add_edge(state, self.trash, letter)

        for letter in self.alphabet:
            self.add_edge(self.trash, self.trash, letter)

        return self

    def merge_states(self, states_to_merge: list):
        new_state = DFA_Node()
        self.states.add(new_state)

        for dfa_state in self.states:
            for key, value in dfa_state.to.items():
                if value in states_to_merge:
                    dfa_state.to[key] = new_state

        for state in states_to_merge:
            for key, value in state.to.items():
                if value in states_to_merge:
                    new_state.to[key] = new_state
                else:
                    new_state.to[key] = value

            if state in self.states:
                self.states.remove(state)

    def minimize(self):
        states_to_merge = []

        for state1 in self.states:
            for state2 in self.states:
                if state1.to == state2.to and state1 != state2:
                    if [state2, state1] not in states_to_merge:
                        states_to_merge.append([state1, state2])

        for pair in states_to_merge:
            print(pair)
            self.merge_states(pair)
