
def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(num):
    if str(num).count("0") > 0:
        return False
    for i in range(1, len(str(num)) // 2 + 1):
        if not is_prime(num):
            return False
        num = int(str(num)[:-i])
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
