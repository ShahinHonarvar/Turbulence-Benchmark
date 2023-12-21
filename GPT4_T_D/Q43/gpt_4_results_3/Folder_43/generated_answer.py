
from sympy import isprime

def find_primes_between_indices(num_list):
    prime_nums = [num for num in num_list[31:93] if isprime(num)]
    prime_nums.sort(reverse=True)
    return prime_nums
