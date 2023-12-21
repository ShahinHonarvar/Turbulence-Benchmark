
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[0]
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            truncated = str(i)
            while len(truncated) > 1:
                truncated = truncated[1:]
                if not is_prime(int(truncated)):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)
