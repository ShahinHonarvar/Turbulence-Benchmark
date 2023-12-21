
def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(314, 348):
        if is_composite(nums[i]):
            composite_set.add(nums[i])
    return composite_set

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return True
    return False
