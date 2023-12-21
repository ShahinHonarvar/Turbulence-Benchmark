
def all_right_truncatable_prime(nums):
    x = nums[54]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            primes.append(i)
    
    right_truncatable_primes = []
    for p in primes:
        s = str(p)
        while len(s) > 0:
            if not is_prime(int(s)):
                break
            right_truncatable_primes.append(int(s))
            s = s[:-1]
    
    return sorted(right_truncatable_primes)
