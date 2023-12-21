
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    
    x = nums[42]
    left_truncatable_primes = [i for i in range(10, x) if is_left_truncatable_prime(i)]
    left_truncatable_primes.sort()
    return left_truncatable_primes
