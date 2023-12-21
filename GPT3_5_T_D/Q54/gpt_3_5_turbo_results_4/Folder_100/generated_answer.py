
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[26]
    result = []
    for num in range(x):
        if is_prime(num):
            num_str = str(num)
            right_truncatable = True
            for i in range(1, len(num_str)):
                truncated_num = int(num_str[:-i])
                if not is_prime(truncated_num):
                    right_truncatable = False
                    break
            if right_truncatable:
                result.append(num)
    return sorted(result)
