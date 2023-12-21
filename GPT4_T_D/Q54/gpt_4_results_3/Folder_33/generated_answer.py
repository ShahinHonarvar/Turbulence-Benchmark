
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    res = []
    for i in range(2, x):
        str_i = str(i)
        if all(isprime(int(str_i[:j])) for j in range(1, len(str_i) + 1)):
            res.append(i)
    res.sort(reverse=True)
    return res
