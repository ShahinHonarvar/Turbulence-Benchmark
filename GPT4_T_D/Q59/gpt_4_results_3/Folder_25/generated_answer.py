
def all_left_truncatable_prime(nums):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_left_truncatable_prime(x):
        if '0' in str(x):
            return False
        length = len(str(x))
        for i in range(length):
            if not is_prime(int(str(x)[i:])):
                return False
        return True

    x = nums[92]
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    
    return sorted(left_truncatable_primes)
