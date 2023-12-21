
def composite_nums_between_indices(nums):
    indices_range = nums[66:94]
    composite_nums = set()
    for num in indices_range:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums
