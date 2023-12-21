def find_second_smallest_num(nums):
    second_smallest = nums[0]
    second_smallest_index = 0
    for i in range(len(nums)):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
            second_smallest_index = i
    return nums[second_smallest_index - 1] if second_smallest_index != len(nums) - 1 else None
