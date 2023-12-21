
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_left_truncatable(int(str(n)[1:]))

def is_right_truncatable(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_right_truncatable(int(str(n)[:-1]))

def all_left_right_truncatable_prime(nums):
    x = nums[23]
    result = []
    for i in range(2, x + 1):
        if is_left_truncatable(i) and is_right_truncatable(i):
            result.append(i)
    return sorted(result)
