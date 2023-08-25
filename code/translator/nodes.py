from lexer import Token


class ExpressionNode:
    pass


class StatementNode(ExpressionNode):
    def __init__(self) -> None:
        super().__init__()
        self.codeStrings = []

    def addNode(self, node: ExpressionNode):
        self.codeStrings.append(node)


class ValueNode(ExpressionNode):
    def __init__(self, value: Token) -> None:
        super().__init__()
        self.value: Token = value


class BinOperatorNode(ExpressionNode):
    def __init__(self, operator: Token, leftNode: ExpressionNode, rightNode: ExpressionNode) -> None:
        super().__init__()
        self.operator: Token = operator
        self.leftNode: ExpressionNode = leftNode
        self.rightNode: ExpressionNode = rightNode


class UnarOperatorNode(ExpressionNode):
    def __init__(self, operator: Token, operand: ExpressionNode) -> None:
        super().__init__()
        self.operator: Token = operator
        self.operand: ExpressionNode = operand


class BlockNode(ExpressionNode):
    def __init__(self, operator: Token, statement: ExpressionNode) -> None:
        super().__init__()
        self.operator: Token = operator
        self.statement: ExpressionNode = statement
        self.body = []

    def addNode(self, node: ExpressionNode):
        self.body.append(node)


class ElseNode(ExpressionNode):
    def __init__(self, operator: Token) -> None:
        super().__init__()
        self.operator: Token = operator
        self.body = []

    def addNode(self, node: ExpressionNode):
        self.body.append(node)
