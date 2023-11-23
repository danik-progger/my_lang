from nodes.expressions.leaf_expressions.LeafExpression import LeafExpression


class Symbol(LeafExpression):
    def __init__(self, char: str):
        super().__init__(char, "SYMBOL")
