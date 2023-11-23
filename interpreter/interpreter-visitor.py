from nodes.Program import Program
from nodes.expressions.leaf_expressions import LeafExpression
from nodes.statements.AssignStatement import AssignStatement
from nodes.statements.PrintStatement import PrintStatement


class InterpreterVisitor:
    def __init__(self) -> None:
        self.variables = {}

    def visit_leaf_expression(self, expression: LeafExpression):
        return expression.value

    def visit_program(self, program: Program):
        program.accept(self)

    def visit_assign_statement(self, statement: AssignStatement):
        self.variables[statement.variable] = statement.expression.accept(self)

    def visit_print_statement(self, statement: PrintStatement):
        print(statement.expression.accept(self))
