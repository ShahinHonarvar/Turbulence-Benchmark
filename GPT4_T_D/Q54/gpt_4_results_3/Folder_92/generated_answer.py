
def all_right_truncatable_prime(nums):
    x = nums[7]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable(n):
        str_n = str(n)
        while len(str_n) > 0:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
        return True
    
    truncatable_primes = []
    for n in range(2, x):
        if is_right_truncatable(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)
