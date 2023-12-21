def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(10, 100):
        if len(nums) > i and len(nums) > i + 1:
            if nums[i] < nums[i + 1]:
                second_smallest_num = nums[i]
            elif nums[i] == nums[i + 1]:
                second_smallest_num = nums[i]
    return second_small smallest_num
