
def all_left_right_truncatable_prime(nums):
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        for i in range(len(str_p)):
            if not is_prime(int(str_p[i:])) or not is_prime(int(str_p[:i+1])):
                return False
        return True

    x = nums[25]
    result = [i for i in range(11, x+1) if is_truncatable(i)]
    
    return sorted(result, reverse=True)
