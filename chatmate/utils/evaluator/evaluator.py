import math
from chatmate.utils.evaluator.parser import Parser

functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'log': math.log10,
    'ln': math.log,
    'abs': abs
}

operators = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y),
    '^': (3, lambda x, y: x ** y),
    '!': (4, math.factorial)
}


class Evaluator:

    def __init__(self):
        pass

    def evaluate(self, expression):
        parser = Parser(expression, operators)
        tokens = parser.tokenize()
        postfix = parser.convert_to_postfix(tokens)
        result = self._postfix_eval(postfix)
        return result


    def _postfix_eval(self, postfix):
        op_stack = []
        for token in postfix:
            if token.type == 0:
                op_stack.append(token.value)
            elif token.type == 2:
                if token.value in functions:
                    arg = op_stack.pop()
                    result = functions[token.value](arg)
                    op_stack.append(result)
                else:
                    raise ValueError(f"Unknown function: {token.value}")
            elif token.type == 1:
                if token.value == '!':
                    if len(op_stack) < 1:
                        raise ValueError("Insufficient operands for factorial")
                    operand = int(op_stack.pop())
                    result = operators[token.value][1](operand)
                    op_stack.append(result)
                else:
                    if len(op_stack) < 2:
                        raise ValueError("Insufficient operands for operator")
                    right_operand = op_stack.pop()
                    left_operand = op_stack.pop()
                    result = operators[token.value][1](left_operand, right_operand)
                    op_stack.append(result)
        if len(op_stack) != 1:
            raise ValueError("Invalid expression")
        return op_stack[0]

