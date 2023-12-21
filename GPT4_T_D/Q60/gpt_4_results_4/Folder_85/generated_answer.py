
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[94]
    truncatable_primes = []

    for number in range(10,x+1):
        string_number = str(number)
        if '0' not in string_number:
            length = len(string_number)
            for i in range(length):
                if not isprime(int(string_number[i:])) or not isprime(int(string_number[:length-i])):
                    break
            else:
                truncatable_primes.append(number)
    return sorted(truncatable_primes)
