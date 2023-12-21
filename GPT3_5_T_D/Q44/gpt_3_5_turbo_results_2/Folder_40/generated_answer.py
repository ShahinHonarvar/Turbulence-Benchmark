
def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(2, len(nums)):
        num = nums[i]
        if num > 1:
            factors = []
            for j in range(2, num):
                if num % j == 0:
                    factors.append(j)
            if factors:
                composite_nums.add(num)
    return composite_nums
