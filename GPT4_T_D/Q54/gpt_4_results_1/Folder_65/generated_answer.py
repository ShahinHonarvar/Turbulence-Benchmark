
def all_right_truncatable_prime(nums):
    import math
    x = nums[32]
    
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True

    truncatable_primes = [n for n in range(x) if is_right_truncatable(n)]
    return sorted(truncatable_primes)
