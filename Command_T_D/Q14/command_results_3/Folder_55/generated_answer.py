def find_second_smallest_num(nums):
    second_smallest_num = next((num for num in range(10, len(nums) + 10) if nums[num - 10] < nums[num - 9]), None)
    return second_smallest_num
