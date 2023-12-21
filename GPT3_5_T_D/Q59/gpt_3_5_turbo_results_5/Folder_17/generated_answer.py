
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_truncatable_prime(n):
        digits = str(n)
        if '0' in digits:
            return False
        for i in range(len(digits)):
            if not is_prime(int(digits[i:])):
                return False
        return True
    
    x = nums[36]
    left_truncatable_primes = []
    for num in range(x-1, 10, -1):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)
