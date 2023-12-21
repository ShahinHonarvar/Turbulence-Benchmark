
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        if len(str(n)) == 1 or len(str(n)) == 2:
            return is_prime(n)
        if is_prime(n):
            return is_truncatable_prime(int(str(n)[1:])) and is_truncatable_prime(int(str(n)[:-1]))
        return False
    
    x = nums[88]
    result = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)
