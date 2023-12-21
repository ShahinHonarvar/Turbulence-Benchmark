def find_second_smallest_num(nums):
    return next((num for num in nums[660:925] if nums[660:925].index(num) == 1), None)
