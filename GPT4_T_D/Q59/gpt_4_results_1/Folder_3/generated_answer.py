
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[100]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        prime = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                prime=False
                break
        if prime:
            primes.append(num)
    return sorted(primes)
