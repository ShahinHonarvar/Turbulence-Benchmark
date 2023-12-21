
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 1:
            return False
        for y in range(2, n):
            if n % y == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_num = str(n)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:len(str_num) - i]))):
                return False
        return True

    x = nums[36]
    res = []
    for i in range(10, x + 1):
        if is_prime(i) and is_left_right_truncatable(i):
            res.append(i)
    return sorted(res)
