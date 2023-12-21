def find_second_smallest_num(nums):
    res = next((el for i, el in enumerate(nums[3:-1]) if i == 4 or i == 5 and el < nums[4]), None)
    return res
