
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    if len(nums) > 26:
        x = nums[26]
        left_right_truncatable_primes = []
        for i in range(10, x + 1):
            if '0' not in str(i):
                truncatable = True
                for j in range(1, len(str(i))):
                    if not (isprime(int(str(i)[j:])) and isprime(int(str(i)[:-j]))):
                        truncatable = False
                        break
                if truncatable and isprime(i):
                    left_right_truncatable_primes.append(i)
        left_right_truncatable_primes.sort()
        return left_right_truncatable_primes
    else:
        return []
