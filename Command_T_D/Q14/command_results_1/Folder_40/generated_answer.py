def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1]:
            second_smallest = nums[i]
            break
    return second_smallest
