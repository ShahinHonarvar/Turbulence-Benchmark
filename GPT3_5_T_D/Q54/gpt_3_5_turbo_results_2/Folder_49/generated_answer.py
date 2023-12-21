
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[14]
    result = []

    for i in range(2, x):
        num_str = str(i)
        truncated = True

        while truncated and len(num_str) > 0:
            if not is_prime(int(num_str)):
                break
            num_str = num_str[:-1]
        else:
            result.append(i)

    return result
