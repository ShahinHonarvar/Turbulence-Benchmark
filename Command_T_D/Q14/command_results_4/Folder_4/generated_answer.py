def find_second_smallest_num(nums):
    result = None
    for i in range(70, 85):
        if nums[i] <= nums[i-1]:
            result = nums[i]
            break
    return result
