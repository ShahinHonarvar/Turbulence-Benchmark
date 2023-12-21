
import sympy

def all_left_right_truncatable_prime(nums):
    x = nums[126]
    primes = []

    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        temp = str(i)
        is_truncatable = True
        while len(temp) > 1:
            temp = temp[1:-1]
            if not (sympy.isprime(int(temp))):
                is_truncatable = False
                break
        
        if is_truncatable and sympy.isprime(i):
            primes.append(i)
            
    return sorted(primes, reverse=True)
