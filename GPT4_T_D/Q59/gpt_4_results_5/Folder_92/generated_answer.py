
from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[7]
    prime_list = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        left_truncations = [num_str[i:] for i in range(len(num_str))]
        if all(isprime(int(n)) for n in left_truncations):
            prime_list.append(num)
    return sorted(prime_list)
