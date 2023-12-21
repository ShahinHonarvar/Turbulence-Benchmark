
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            left_num = int(num_str[i:])
            right_num = int(num_str[:len(num_str) - i])
            if not is_prime(left_num) or not is_prime(right_num):
                return False
        return True

    x = nums[46]
    result = []
    for num in range(x, 0, -1):
        if is_truncatable_prime(num):
            result.append(num)
    return result
