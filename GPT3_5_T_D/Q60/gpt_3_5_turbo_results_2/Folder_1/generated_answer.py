
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
        for i in range(len(str_num)):
            if str_num[i] == '0':
                return False
            if not is_prime(int(str_num[i:])):
                return False
            if not is_prime(int(str_num[:i+1])):
                return False
        return True

    x = nums[20]
    result = []
    for num in range(x, 1, -1):
        if is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result
