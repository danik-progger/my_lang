from automatons.nodes.node import AutomatonNode


class NFA_Node(AutomatonNode):
    def __init__(self):
        super().__init__()
        self.to = dict()
        self.by_eps = set()
