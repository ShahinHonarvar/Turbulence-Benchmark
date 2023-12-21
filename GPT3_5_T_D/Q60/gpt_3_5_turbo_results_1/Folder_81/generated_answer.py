
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for num in range(2, int(n**0.5) + 1):
            if n % num == 0:
                return False
        return True
    
    def is_left_truncatable_prime(n):
        while n >= 10:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return is_prime(n)
    
    def is_right_truncatable_prime(n):
        while n >= 10:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return is_prime(n)
    
    x = nums[98]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            result.append(num)
    
    return sorted(result)
