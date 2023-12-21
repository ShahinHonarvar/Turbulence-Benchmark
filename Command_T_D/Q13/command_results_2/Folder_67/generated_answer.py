
def find_second_largest_num(nums):
    second_largest = max(nums[22:50])
    if second_largest in nums:
        return second_largest
    else:
        return None
