def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Avoid division by zero
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Example usage:
result = simple_calculator(5, 3, '+')
print(result)  # Output: 8

result = simple_calculator(10, 2, '/')
print(result)  # Output: 5.0

result = simple_calculator(7, 0, '/')
print(result)  # Output: Error: Division by zero

result = simple_calculator(4, 2, '%')
print(result)  # Output: Error: Invalid operator
