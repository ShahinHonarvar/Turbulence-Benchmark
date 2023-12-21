
from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[6]
    result = []
    for number in range(2, x):
        str_num = str(number)
        prime = all(isprime(int(str_num[:i])) for i in range(1, len(str_num)+1))
        if prime:
            result.append(number)
    result.sort(reverse=True)
    return result
