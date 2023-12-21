
from sympy import isprime
from itertools import permutations

def all_left_truncatable_prime(tuple):
    def is_left_prime(num):
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True

    x = tuple[32]
    numbers = ['1', '2', '3', '5', '7', '9']
    prime_numbers = set()
    for length in range(1, len(str(x))):
        for num_tuple in permutations(numbers, length):
            num = int(''.join(num_tuple))
            if num < x and is_left_prime(num):
                prime_numbers.add(num)
    return sorted(list(prime_numbers))
