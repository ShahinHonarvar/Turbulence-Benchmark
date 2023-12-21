
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def left_truncate(n):
        str_n = str(n)
        for _ in range(1, len(str_n)):
            str_n = str_n[1:]
            if not is_prime(int(str_n)):
                return False
        return True
    
    def right_truncate(n):
        str_n = str(n)
        for _ in range(1, len(str_n)):
            str_n = str_n[:-1]
            if not is_prime(int(str_n)):
                return False
        return True
    
    x = nums[52]
    result = []
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        if is_prime(num) and left_truncate(num) and right_truncate(num):
            result.append(num)
    return sorted(result, reverse=True)
