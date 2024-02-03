def find_max_min(tuple_of_integers):
    
    if not tuple_of_integers:
        return None, None

    
    max_value = min_value = tuple_of_integers[0]

    
    for num in tuple_of_integers:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num

    return max_value, min_value


my_tuple = (3, 8, 1, 5, 7, 2, 6, 4)
max_value, min_value = find_max_min(my_tuple)

print("Tuple:", my_tuple)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
