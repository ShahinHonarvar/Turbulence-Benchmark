def find_second_smallest_num(nums):
    second_smallest = next((i for i in range(50, 200) if nums[i] < nums[nums[i]]), None)
    return nums[second_smallest]
