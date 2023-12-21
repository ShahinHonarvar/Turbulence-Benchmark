
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = nums[645]
    right_truncatable_primes = []
    
    def check_truncatable_prime(n):
        if not is_prime(n):
            return False
        if n < 10:
            return True
        return check_truncatable_prime(n // 10)
    
    for i in range(x-1, 1, -1):
        if check_truncatable_prime(i):
            right_truncatable_primes.append(i)
    
    return sorted(right_truncatable_primes)
