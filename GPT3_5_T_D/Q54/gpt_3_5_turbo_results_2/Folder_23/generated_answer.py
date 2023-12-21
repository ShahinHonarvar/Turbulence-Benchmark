
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(nums):
    x = nums[77]
    res = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            res.append(i)

    return sorted(res, reverse=True)
