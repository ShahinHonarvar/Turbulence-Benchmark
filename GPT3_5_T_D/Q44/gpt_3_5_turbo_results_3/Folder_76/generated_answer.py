
def composite_nums_between_indices(nums):
    composite_nums = []
    for i in range(639, 976):
        if i >= len(nums):
            break
        num = nums[i]
        if num > 1:
            is_composite = False
            for j in range(2, int(num/2) + 1):
                if num % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.append(num)

    return set(composite_nums)
