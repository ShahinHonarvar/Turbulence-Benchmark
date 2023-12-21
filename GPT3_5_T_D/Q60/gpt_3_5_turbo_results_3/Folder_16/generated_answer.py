
def all_left_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_left_right_truncatable(num):
        str_num = str(num)
        while len(str_num) > 1:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:-1]
        return True
    
    x = nums[792]
    result = []
    for i in range(2, x+1):
        if '0' not in str(i) and is_left_right_truncatable(i):
            result.append(i)
    return sorted(result)
