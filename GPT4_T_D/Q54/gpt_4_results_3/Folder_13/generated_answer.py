
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True

    x = nums[784]
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
