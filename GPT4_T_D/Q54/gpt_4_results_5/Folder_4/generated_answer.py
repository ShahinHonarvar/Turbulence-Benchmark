
from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[96]
    def is_right_truncatable(n):
        n = str(n)
        return all(isprime(int(n[:-i])) for i in range(len(n)))

    all_nums = list(filter(is_right_truncatable, range(2, x)))
    all_nums.sort(reverse=True)
    return all_nums
