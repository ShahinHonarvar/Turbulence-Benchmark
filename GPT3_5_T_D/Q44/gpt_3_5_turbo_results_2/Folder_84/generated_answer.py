
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(30, 49):
        if is_composite(nums[i]):
            composites.add(nums[i])
    return composites

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return True
    return False
