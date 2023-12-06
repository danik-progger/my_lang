from interpreter.antlr.nodes.expressions.Expression import Expression


class IfStatement:
    def __init__(self, condition: Expression, expressions: list[Expression]):
        self.condition = ondition
        self.expressions = expressions

    def accept(self, visitor):
        return visitor.visit_if_statement(self)
