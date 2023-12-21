
def all_left_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                return False
        return True

    x = nums[14]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)
