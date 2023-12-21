def composite_nums_between_indices(nums):
    result = set()
    for i in range(10, 66):
        if not is_prime(nums[i]):
            result.add(nums[i])
    return result
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = n**0.5
    for num in range(5, maxDivisor, 6):
        if n % num == 0:
            return False
    return True
