
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[23]
    result = []
    for num in range(2, x):
        num_str = str(num)
        while num_str:
            if is_prime(int(num_str)):
                num_str = num_str[:-1]
            else:
                break
        if not num_str:
            result.append(num)
    return sorted(result)
