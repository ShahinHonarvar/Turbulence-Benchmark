
def all_left_right_truncatable_prime(nums):
    import math
    
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        elif n > 2 and n % 2 == 0:
            return False
        else:
            max_div = math.floor(math.sqrt(n))
            for i in range(3, 1 + max_div, 2):
                if n % i == 0:
                    return False
            return True

    def is_lr_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
                return False
        return True
    
    x = nums[7]
    truncatable_primes = []
    for i in range(10, x+1):
        if is_lr_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
