
def find_second_largest_num(nums):
    result = sorted(nums)[30]
    if nums[result] == result:
        return nums[result]
    else:
        return None
