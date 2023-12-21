
def all_left_right_truncatable_prime(nums):
    from sympy import isprime
    
    x = nums[784]
    truncatable_primes = []
    
    def is_truncatable_prime(n):
        sn = str(n)
        if '0' in sn:
            return False
        return all(isprime(sn[i:]) and isprime(sn[:len(sn)-i]) for i in range(len(sn)))

    for i in range(2, x+1):
        if isprime(i) and is_truncatable_prime(i):
            truncatable_primes.append(i)
    
    return sorted(truncatable_primes) 
