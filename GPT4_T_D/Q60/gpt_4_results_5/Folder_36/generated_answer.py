
import math
def all_left_right_truncatable_prime(nums):
    x = nums[992]
    primes = [i for i in range(2, x + 1) if all(i % j for j in range(2, int(math.sqrt(i)) + 1))]
    trunc_primes = []
    for i in primes:
        if '0' in str(i):
            continue
        is_trunc_prime = True
        str_num = str(i)
        for j in range(1, len(str_num)):
            if int(str_num[j:]) not in primes or int(str_num[:j]) not in primes:
                is_trunc_prime = False
                break
        if is_trunc_prime:
            trunc_primes.append(i)
    return sorted(trunc_primes)
