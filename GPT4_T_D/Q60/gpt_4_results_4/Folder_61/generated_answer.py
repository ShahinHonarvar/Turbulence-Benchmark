
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(t):
    def generate_numbers():
        digits = '123456789'
        for l in range(2, len(str(t[3]))):
            for number_tuple in product(digits, repeat=l):
                yield ''.join(number_tuple)

    def is_left_right_prime(n):
        return all(isprime(int(n[i: -j])) for i in range(len(n)) for j in range(len(n)))
    
    result = [int(number) for number in generate_numbers() if is_left_right_prime(number) and int(number) <= t[3]]
    return sorted(result, reverse=True)
