
def all_left_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_truncatable_prime(num):
        for i in range(len(str(num))):
            trunc_num = int(str(num)[i:])
            if not is_prime(trunc_num):
                return False
            trunc_num = int(str(num)[:i+1])
            if not is_prime(trunc_num):
                return False
        return True
    
    x = nums[74]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
