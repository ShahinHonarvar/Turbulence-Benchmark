
def all_right_truncatable_prime(nums):
    x = nums[32]
    all_primes = set()
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i])) for i in range(1, len(str_n) + 1))
    
    for i in range(2, x):
        if is_right_truncatable(i):
            all_primes.add(i)
    
    return sorted(list(all_primes))
