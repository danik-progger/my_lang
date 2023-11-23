from nodes.expressions.leaf_expressions.LeafExpression import LeafExpression


class Number(LeafExpression):
    def __init__(self, num: int):
        super().__init__(num, "NUM")
