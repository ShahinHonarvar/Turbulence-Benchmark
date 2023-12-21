
def find_second_largest_num(nums):
    second_largest = max(nums[:52] + nums[71:], key=lambda x: nums.count(x))
    return second_largest
