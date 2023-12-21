def composite_nums_between_indices(nums):
    if len(nums) == 0:
        return set()
    max_num = nums[0]
    min_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
        if nums[i] < min_num:
            min_num = nums[i]
    if min_num > max_num:
        return set()
    return {num for num in range(min_num, max_num + 1) if num % 2 == 1 and num % 3 == 0}
