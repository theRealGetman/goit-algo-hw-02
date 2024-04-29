opening_brackets = "({["
closing_brackets = ")}]"
pairs = {")": "(", "}": "{", "]": "["}


def is_balanced(expression):
    stack = []

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != pairs[char]:
                return "Несиметрично"
    return "Симетрично" if not stack else "Несиметрично"


# Приклад використання
expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expr in expressions:
    print(expr + ": " + is_balanced(expr))
