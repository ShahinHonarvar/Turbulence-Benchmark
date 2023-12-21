
from itertools import product
from sympy import isprime

def generate_candidates(n):
    candidates_set = set()

    for i in range(1, n):
        candidates_set.update(map(int, (''.join(map(str, p)) for p in product(range(1, 10), repeat=i))))

    return sorted(candidates_set)

def check_left_truncatable(n):
    n_str = str(n)

    return all(isprime(int(n_str[i:])) for i in range(len(n_str)))

def all_left_truncatable_prime(t):
    x = t[42]
    candidates = generate_candidates(len(str(x)))

    return list(filter(check_left_truncatable, (i for i in candidates if i < x)))
