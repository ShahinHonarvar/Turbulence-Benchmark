
def composite_nums_between_indices(nums):
    composite_nums_set = set()
    for i in range(25, 60):
        if i < len(nums):
            num = nums[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_nums_set.add(num)
                        break
    return composite_nums_set
