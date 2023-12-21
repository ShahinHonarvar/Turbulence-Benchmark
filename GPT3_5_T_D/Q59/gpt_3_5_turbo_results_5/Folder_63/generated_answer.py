
def all_left_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    x = nums[88]
    result = []
    for n in range(2, x):
        str_num = str(n)
        if '0' not in str_num:
            is_left_truncatable = True
            for i in range(len(str_num)):
                if not is_prime(int(str_num[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(n)
    
    return sorted(result)
