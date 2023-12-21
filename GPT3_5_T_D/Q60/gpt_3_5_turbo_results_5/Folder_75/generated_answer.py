
def all_left_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
      
    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
            if not is_prime(int(str_num[:i+1])):
                return False
        return True
      
    x = nums[41]
    result = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result)
