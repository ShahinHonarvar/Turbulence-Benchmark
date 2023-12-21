def find_second_smallest_num(nums):
    return next((num for num in nums[70:84+1] if num < nums[70]), None)
