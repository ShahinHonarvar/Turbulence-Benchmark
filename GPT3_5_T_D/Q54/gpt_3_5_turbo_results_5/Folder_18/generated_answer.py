
def all_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        str_num = str(num)
        while str_num != "":
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True

    x = nums[429]
    result = []
    for i in range(x - 1, 1, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
