
def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(246, 751):
        if i < len(nums):
            num = nums[i]
            if num > 1 and any(num % j == 0 for j in range(2, int(num ** 0.5) + 1)):
                composite_nums.add(num)
    return composite_nums
