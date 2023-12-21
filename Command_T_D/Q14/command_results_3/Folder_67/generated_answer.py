def find_second_smallest_num(nums):
    if len(nums) < 50:
        return None
    index = 50
    while index < len(nums) - 1:
        if nums[index] > nums[index + 1]:
            break
        index += 1
    return nums[index - 1]
