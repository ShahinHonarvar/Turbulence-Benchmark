
def find_second_largest_num(nums):
    result = next((el for el in nums[56:98+1] if el > nums[95]), None)
    return result
