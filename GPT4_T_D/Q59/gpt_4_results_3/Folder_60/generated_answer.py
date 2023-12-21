
from itertools import permutations
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[87]
    numbers = [str(i) for i in range(1,10)]
    results = []

    def truncatable(num):
        return all(isprime(int(num[i:])) for i in range(len(num)))
    
    for r in range(2, len(str(x))):
        for p in permutations(numbers, r):
            num = ''.join(p)
            if truncatable(num):
                results.append(int(num))
    return sorted(n for n in results if n < x)
