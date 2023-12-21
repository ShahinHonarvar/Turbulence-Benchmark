
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(20, 201):
        if i >= len(nums):
            break
        if is_composite(nums[i]):
            composites.add(nums[i])
    return composites

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False
