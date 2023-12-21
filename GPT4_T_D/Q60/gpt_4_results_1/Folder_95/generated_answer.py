
def all_left_right_truncatable_prime(nums):
    x = nums[77]
    
    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:i])):
                return False
        return True
    
    truncatable_primes = [i for i in range(10, x+1) if is_prime(i) and is_truncatable(i)]
    
    return sorted(truncatable_primes)
