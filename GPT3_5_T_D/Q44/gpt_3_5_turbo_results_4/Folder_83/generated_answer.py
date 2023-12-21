
def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(111, len(nums)):
        if is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False
