
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[78]
    trunc_primes = []

    for i in range(11, x + 1):
        if '0' in str(i):
            continue
        str_i = str(i)
        length = len(str_i)
        for j in range(length):
            if not (isprime(int(str_i[j:])) and isprime(int(str_i[:length-j]))):
                break
        else:
            trunc_primes.append(i)

    return sorted(trunc_primes, reverse=True)
