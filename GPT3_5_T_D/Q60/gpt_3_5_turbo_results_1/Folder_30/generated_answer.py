
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
    str_n = str(n)
    for i in range(len(str_n)):
        left = str_n[i:]
        right = str_n[:i+1]
        if not is_prime(int(left)) or not is_prime(int(right)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[37]
    result = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
