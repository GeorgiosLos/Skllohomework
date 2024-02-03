def hash_list(input_list):
    
    tuple_representation = tuple(input_list)

   
    hash_value = hash(tuple_representation)

    return hash_value


my_list = [1, 2, 3, 'apple', 'banan', 'George']
hash_result = hash_list(my_list)

print("Original List:", my_list)
print("Hash Value:", hash_result)
