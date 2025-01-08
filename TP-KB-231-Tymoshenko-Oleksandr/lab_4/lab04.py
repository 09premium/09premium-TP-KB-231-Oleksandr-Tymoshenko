class ReversePolishNotation:
    def __init__(self):
        self.operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def is_operator(self, token):
        return token in self.operators

    def precedence(self, operator):
        return self.operators.get(operator, 0)

    def infix_to_postfix(self, expression):
        stack = []
        output = []
        for token in expression:
            if token.isnumeric():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif self.is_operator(token):
                while (stack and stack[-1] != '(' and
                       self.precedence(stack[-1]) >= self.precedence(token)):
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return output

    def evaluate_postfix(self, expression):
        stack = []
        for token in expression:
            if token.isnumeric():
                stack.append(float(token))
            elif self.is_operator(token):
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)
        return stack[0]

if __name__ == "__main__":
    rpn = ReversePolishNotation()

    # Ввод математического выражения
    infix_expression = input("Enter a mathematical expression: ")
    tokens = []
    temp = ''

    for char in infix_expression:
        if char.isnumeric() or char == '.':
            temp += char
        else:
            if temp:
                tokens.append(temp)
                temp = ''
            if char.strip():
                tokens.append(char)
    if temp:
        tokens.append(temp)

    # Преобразование в ОПЗ
    postfix_expression = rpn.infix_to_postfix(tokens)
    print("Postfix notation:", ' '.join(postfix_expression))

    # Вычисление результата
    result = rpn.evaluate_postfix(postfix_expression)
    print("Result:", result)
