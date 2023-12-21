
def find_second_largest_num(nums):
    second_largest_num = max(nums[8:9])
    if second_largest_num in nums[8:9]:
        return second_largest_num
    else:
        return None
