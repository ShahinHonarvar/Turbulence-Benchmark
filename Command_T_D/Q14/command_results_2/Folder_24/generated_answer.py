def find_second_smallest_num(nums):
    second_smallest = nums[23]
    i = 23
    while i > 0:
        i -= 1
        if nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest
