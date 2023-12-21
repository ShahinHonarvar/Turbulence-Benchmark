
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    res = []
    for i in range(2, x):
        str_i = str(i)
        if '0' in str_i:
            continue
        if all(isprime(int(str_i[j:])) for j in range(len(str_i))):
            res.append(i)
    return sorted(res, reverse=True)
