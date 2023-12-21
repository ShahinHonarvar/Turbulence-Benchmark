
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[37]

    def is_left_truncatable_prime(num: str) -> bool:
        return all(isprime(int(num[i:])) for i in range(len(num)))

    res = []
    for num in range(2, x):
        if "0" not in str(num) and is_left_truncatable_prime(str(num)):
            res.append(num)
    return sorted(res, reverse=True)
