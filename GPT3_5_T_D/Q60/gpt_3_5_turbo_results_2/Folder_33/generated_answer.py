
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        left = str(n)
        right = str(n)
        while len(left) > 2:
            left = left[1:]
            right = right[:-1]
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
        return True
    
    x = nums[945]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            primes.append(num)
    
    return sorted(primes, reverse=True)
