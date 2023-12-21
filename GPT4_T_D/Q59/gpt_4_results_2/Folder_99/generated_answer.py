
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[758]

    def left_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not isprime(int(n_str[i:])):
                return False
        return True

    primes = []
    for num in range(2,x):
        if '0' not in str(num) and isprime(num) and left_truncatable(num):
            primes.append(num)

    return sorted(primes)
