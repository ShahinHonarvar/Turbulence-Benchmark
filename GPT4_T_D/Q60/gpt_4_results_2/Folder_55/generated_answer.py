
from itertools import permutations
from sympy import isprime

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[73]

    left_and_right_truncatable_primes = []
    digits = '123456789'
    for i in range(1, len(str(x)) + 1):
        perms = [''.join(p) for p in permutations(digits, i)]

        for num in perms:
            if int(num) > x:
                continue
            ltr = all(isprime(int(num[n:])) for n in range(len(num)))
            rtl = all(isprime(int(num[:n+1])) for n in range(len(num), 0, -1))
            if ltr and rtl:
                left_and_right_truncatable_primes.append(int(num))

    return sorted(left_and_right_truncatable_primes, reverse=True)
