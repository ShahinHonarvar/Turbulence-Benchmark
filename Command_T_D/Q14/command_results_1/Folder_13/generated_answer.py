def find_second_smallest_num(nums):
    second_smallest = next(
        i
        for i in range(28, 33)
        if nums[i - 1] < nums[i]
    )
    return nums[second_smallest]
