def all_left_truncatable_prime(nums):
    return sorted(filter(left_truncatable_prime, list(range(1, nums[67] + 1))), reverse=True)
def left_truncatable_prime(n):
    if not n:
        return True
    if n % 2 == 0:
        return False
    s = str(n)
    while s[0] != '2':
        if not s[0] in '23456789':
            return False
        s = s[1:]
    return True
