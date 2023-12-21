
from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[57]
    def truncate(num):
        return [int(str(num)[i:]) for i in range(len(str(num)))]

    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        else:
            return all(isprime(i) for i in truncate(num))

    res = [i for i in range(2, x) if is_left_truncatable(i)]
    return sorted(res, reverse=True)
