
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:i])) or not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[3]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and '0' not in str(i) and is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result
