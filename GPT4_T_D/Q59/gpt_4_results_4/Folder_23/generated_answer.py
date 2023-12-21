
import sympy

def all_left_truncatable_prime(nums):
    x = nums[77] if len(nums) > 77 else None
    if not x:
        return []
    ltr_primes = []
    for i in range(11, x):
        if "0" in str(i):
            continue
        str_i = str(i)
        if all(sympy.isprime(int(str_i[j:])) for j in range(len(str_i))):
            ltr_primes.append(i)
    ltr_primes.sort(reverse=True)
    return ltr_primes
