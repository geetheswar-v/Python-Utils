from chatmate.utils.evaluator.tokens import Token, TokenType


class Parser:

    def __init__(self, expression, operators):
        self.expression = expression
        self.operators = operators

    def tokenize(self):
        expr = self.expression
        tokens = []
        i = 0
        while i < len(expr):
            if expr[i].isdigit() or expr[i] == '.':
                num = ''
                while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                    num += expr[i]
                    i += 1
                tokens.append(Token(TokenType.NUMBER, float(num)))
            elif expr[i].isalpha():
                func_name = ''
                while i < len(expr) and expr[i].isalpha():
                    func_name += expr[i]
                    i += 1
                tokens.append(Token(TokenType.FUNCTION, func_name))
            elif expr[i] in self.operators:
                tokens.append(Token(TokenType.OPERATOR, expr[i]))
                i += 1
            elif expr[i] == '(' or expr[i] == ')':
                tokens.append(Token(TokenType.PARENTHESIS, expr[i]))
                i += 1
            elif expr[i] == ' ':
                i += 1
            else:
                raise ValueError(f"Invalid expr: {expr[i]}")
        return tokens

    def convert_to_postfix(self, tokens):
        postfix = []
        op_stack = []
        for token in tokens:
            if token.type == 0:
                postfix.append(token)
            elif token.type == 2:
                op_stack.append(token)
            elif token.type == 1:
                while (op_stack and op_stack[-1].type == 1
                       and op_stack[-1].value != '('
                       and self.operators[token.value][0] <= self.operators[op_stack[-1].value][0]):
                    postfix.append(op_stack.pop())
                op_stack.append(token)
            elif token.type == 3:
                if token.value == '(':
                    op_stack.append(token)
                elif token.value == ')':
                    while op_stack and op_stack[-1].value != '(':
                        postfix.append(op_stack.pop())
                    if op_stack and op_stack[-1].value == '(':
                        op_stack.pop()
                    else:
                        raise ValueError("Mismatched parentheses")
        while op_stack:
            if op_stack[-1].type == 3:
                raise ValueError("Mismatched parentheses")
            postfix.append(op_stack.pop())
        return postfix
