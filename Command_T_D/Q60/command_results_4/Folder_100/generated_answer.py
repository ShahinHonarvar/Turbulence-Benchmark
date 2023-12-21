
def all_left_right_truncatable_prime(nums):
    l, r = nums[0], nums[1]
    while l < r:
        m = l + r >> 1
        if is_left_right_truncatable_prime(m):
            return [m]
        l = m + 1
        r = m + 10**5
    return []

def is_left_right_truncatable_prime(n):
    if n < 10:
        return True
    if n % 10 in [0, 5]:
        return False
    if n < 100:
        return True
    if n % 100 in [0, 25]:
        return False
    if n < 1000:
        return True
    if n % 1000 in [0, 375]:
        return False
    if n < 10000:
        return True
    if n % 10000 in [0, 9375]:
        return False
    return True
