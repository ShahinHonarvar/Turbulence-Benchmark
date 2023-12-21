
def all_right_truncatable_prime(nums):
    x = nums[97]
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[:-1]
            if not is_prime(int(str_num)):
                return False
        return True
    
    result = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result)
