
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False

    if not is_prime(n):
        return False

    str_n = str(n)
    for i in range(1, len(str_n)):
        left = int(str_n[:i])
        right = int(str_n[i:])
        if not is_prime(left) or not is_prime(right):
            return False

    return True

def all_left_right_truncatable_prime(nums):
    x = nums[22]
    result = []
    for i in range(x, 1, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return result
