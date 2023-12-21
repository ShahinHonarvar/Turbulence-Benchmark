
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[54]
    primes = []
    for num in range(11, x+1):
        str_num = str(num)
        if '0' not in str_num:
            length = len(str_num)
            values = [str_num[i: j + 1] for i in range(length) for j in range(i + 2, length + 1)]
            truncated_values = set([value for value in values if len(value) >= 2])
            if isprime(num) and all(isprime(int(n)) for n in truncated_values):
                primes.append(num)
    return sorted(primes)
