def all_right_truncatable_prime(nums):
    result = []
    for i in range(2, nums[645] + 1):
        while not is_prime(i):
            i += 1
        result.append(i)
    return result
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1:
        return False
    if n == 5:
        return True
    if n == 0:
        return False
    if n == 4:
        return True
    if n == 6:
        return True
    if n == 8:
        return True
    if n == 9:
        return True
    if n == 7:
        return True
    if n == 2 or n == 3:
        return True
    if n == 1:
        return False
    if n == 5:
        return True
    if n == 0:
        return False
    if n == 4:
        return True
    if n == 6:
        return True
    if n == 8:
        return True
    if n == 9:
        return True
    if n == 7:
        return True
