
def composite_nums_between_indices(nums):
    composites = set()
    for i in range(30, min(88, len(nums))):
        num = nums[i]
        if num > 1 and any(num % d == 0 for d in range(2, int(num**0.5)+1)):
            composites.add(num)
    return composites
