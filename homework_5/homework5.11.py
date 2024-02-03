def is_subset(set1, set2):
    
    return set1.issubset(set2)

setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

result = is_subset(setA, setB)


print(f"Is setA a subset of setB? {result}")
