def composite_nums_between_indices(nums):
    result = set()
    for i in range(0, 4):
        if i < 2:
            break
        elif i == 2:
            result.add(nums[i])
        else:
            for j in range(i, 3):
                if nums[j] % i == 0 and nums[j] / i not in result:
                    result.add(nums[j])
                    break
    return result
