
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[64]
    primes = []

    for potential_prime in range(x, 1, -1):
      potential_prime_str = str(potential_prime)
      if '0' in potential_prime_str:
        continue
      
      left_truncatable = all(isprime(int(potential_prime_str[i:])) for i in range(len(potential_prime_str)))
      right_truncatable = all(isprime(int(potential_prime_str[:i])) for i in range(1, len(potential_prime_str)+1))
  
      if left_truncatable and right_truncatable:
        primes.append(potential_prime)

    return sorted(primes, reverse = True)
