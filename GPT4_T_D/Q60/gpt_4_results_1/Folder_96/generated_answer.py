
from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[29]
    primes = []
    
    for num in range(10, x+1):
        if '0' in str(num): continue
        if not isprime(num): continue
        l_num, r_num = str(num), str(num)
        is_LRT_prime = True
        while len(l_num) > 1 and len(r_num) > 1 and is_LRT_prime:
            l_num, r_num = l_num[1:], r_num[:-1]
            if not isprime(int(l_num)) or not isprime(int(r_num)):
                is_LRT_prime = False
        if is_LRT_prime: primes.append(num)
    return sorted(primes)
