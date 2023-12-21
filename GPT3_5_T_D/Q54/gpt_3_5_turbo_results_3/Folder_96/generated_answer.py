
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = nums[29]
    right_truncatable_primes = []
    
    def check_right_truncatable_prime(n):
        if is_prime(n):
            right_truncatable_primes.append(n)
            for i in range(10):
                next_num = int(str(n) + str(i))
                check_right_truncatable_prime(next_num)
    
    check_right_truncatable_prime(2)
    right_truncatable_primes = [num for num in right_truncatable_primes if num < x]
    right_truncatable_primes.sort()
    
    return right_truncatable_primes
