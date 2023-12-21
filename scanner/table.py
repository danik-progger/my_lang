from automatons.classes.dfa import DFA
from scanner.alphabet import category_for


class Table:
    def __init__(self, dfa: DFA) -> None:
        self.table = {}
        self.error = dfa.trap
        self.start = None
        self.error = None
        self.fill_table(dfa)

    def fill_table(self, dfa: DFA):
        for state in dfa.states:
            if state == dfa.root:
                self.start = state
            elif state == dfa.trap:
                self.error = dfa.trap

            self.table[state] = {}
            for letter in dfa.alphabet:
                self.table[state][category_for(letter)] = state.To(letter)

    def __getitem__(self, state):
        return self.table[state]
