
def composite_nums_between_indices(nums):
    composite_nums = []
    for i in range(8, 10):
        num = nums[i]
        if num>1:
            for j in range(2, num):
                if (num%j) == 0:
                    composite_nums.append(num)
                    break
    return set(composite_nums)
