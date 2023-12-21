
def all_left_right_truncatable_prime(nums):
    x = nums[42]
    lst = []
    
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5)+1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True
    
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        str_num = str(num)
        for i in range(len(str_num)):
            left = str_num[i:]
            right = str_num[:len(str_num) - i]
            if not is_prime(int(left)) or not is_prime(int(right)):
                break
        else:
            lst.append(num)
    return sorted(lst)
