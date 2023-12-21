
def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(262, 747):
        num = nums[i]
        if num > 1:
            for j in range(2, int(num/2)+1):
                if (num % j) == 0:
                    composite_set.add(num)
                    break
    return composite_set
