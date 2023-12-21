
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[57]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        lt = [int(str(num)[i:]) for i in range(len(str(num)))]
        rt = [int(str(num)[:i + 1]) for i in range(len(str(num)))]
        if all(isprime(n) for n in lt) and all(isprime(n) for n in rt):
            primes.append(num)
    primes.sort(reverse=True)
    return primes
