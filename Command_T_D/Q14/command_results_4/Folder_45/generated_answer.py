def find_second_smallest_num(nums):
    second_smallest = next(i for i in range(30, 201) if nums[i] < nums[i - 1])
    return nums[second_smallest] if second_smallest < len(nums) else None
