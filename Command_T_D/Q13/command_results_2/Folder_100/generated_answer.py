
def find_second_largest_num(nums):
    second_largest = max(nums[42:68], key=lambda x: nums.count(x))
    return second_largest if second_largest in nums else None
