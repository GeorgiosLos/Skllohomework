def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_numbers_set = {num for num in range(2, 100) if is_prime(num)}


print("Set of prime numbers less than 100:", prime_numbers_set)
