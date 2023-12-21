
def all_right_truncatable_prime(nums):
    x = nums[14]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
  
    truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    truncatable_primes.sort()
  
    return truncatable_primes
