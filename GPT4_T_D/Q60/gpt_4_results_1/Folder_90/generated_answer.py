
from itertools import permutations
from math import sqrt

def all_left_right_truncatable_prime(tuple_of_integers):
    def is_prime(n):
        if n == 1: 
            return False
        for k in range(2, int(sqrt(n) + 1)):
            if n % k == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = tuple_of_integers[466]
    truncatable_primes = []
    for length in range(1, len(str(x)) + 1):
        for comb in permutations('123456789', length):
            number = int(''.join(comb))
            if number <= x and is_truncatable(number):
                truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)
