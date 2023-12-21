
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[126]
    left_truncatable_primes = []
    for num in range(10, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        nums_list = [int(num_str[i:]) for i in range(len(num_str))]
        if all(isprime(i) for i in nums_list):
            left_truncatable_primes.append(nums_list[0])
    return sorted(left_truncatable_primes, reverse=True)
