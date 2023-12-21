
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        if len(num_str) == 1 or len(num_str) == 2:
            return is_prime(n)
        left_truncatable = is_truncatable_prime(int(num_str[1:]))
        right_truncatable = is_truncatable_prime(int(num_str[:-1]))
        return is_prime(n) and left_truncatable and right_truncatable
    
    x = nums[96]
    truncatable_primes = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
