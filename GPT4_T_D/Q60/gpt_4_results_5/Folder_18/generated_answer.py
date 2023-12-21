
def all_left_right_truncatable_prime(nums):
    x = nums[429]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            left_removed = int(str(n)[i:])
            right_removed = int(str(n)[:-i])
            if not is_prime(left_removed) or not is_prime(right_removed):
                return False
        return True

    truncatable_primes = [i for i in range(11, x + 1) 
                          if is_prime(i) and is_left_right_truncatable_prime(i)]
    
    return sorted(truncatable_primes, reverse=True)
