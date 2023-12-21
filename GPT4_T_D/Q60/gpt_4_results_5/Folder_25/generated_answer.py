
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[92]
    prime_list = [2, 3, 5, 7]
    truncatable_primes = []

    for num_length in range(2, len(str(x))):
        numbers = list(product(prime_list, repeat=num_length))
        for num_tuple in numbers:
            num_string = ''.join(map(str, num_tuple))
            num = int(num_string)
            if num <= x and num_string.find('0') == -1:
                if all(isprime(int(num_string[i:])) and isprime(int(num_string[:-i])) for i in range(num_length)):
                    truncatable_primes.append(num)
    return sorted(truncatable_primes)
