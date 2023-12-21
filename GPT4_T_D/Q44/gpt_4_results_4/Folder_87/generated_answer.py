
def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(43, 52):
         if i < len(nums) and not is_prime(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
