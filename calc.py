def compute(expression):
    """Perform simple arithmetic encoded in an input string.

    For example, '1 + 2' returns 3, and '1 - 2' returns -1.
    """
    num0, operator, num1 = expression.split(' ')
    num0, num1 = float(num0), int(num1)
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        print('unknown operator!')
        return None
