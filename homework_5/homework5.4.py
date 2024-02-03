def sum_of_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sum(even_numbers)


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers_list)

print("List:", numbers_list)
print("Sum of even numbers:", result)
