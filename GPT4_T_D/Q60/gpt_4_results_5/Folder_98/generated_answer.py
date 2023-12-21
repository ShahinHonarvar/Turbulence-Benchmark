
from itertools import permutations
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[8]
    primes = ['2', '3', '5', '7']
    possible_numbers = []
    for i in range(2, len(str(x)) + 1):
        for num in permutations(primes, i):
            possible_numbers.append(''.join(num))

    possible_numbers = [int(num) for num in possible_numbers if int(num) <= x]
    lrt_primes = []
    for num in possible_numbers:
        string_num = str(num)
        for i in range(len(string_num)):
            left_truncated = string_num[i:]
            right_truncated = string_num[:len(string_num) - i]
            if not isprime(int(left_truncated)) or not isprime(int(right_truncated)):
                break
        else:
            lrt_primes.append(num)

    return sorted(lrt_primes, reverse=True)
