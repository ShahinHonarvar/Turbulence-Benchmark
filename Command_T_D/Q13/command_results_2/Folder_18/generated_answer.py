
def find_second_largest_num(nums):
    a = sorted(nums)[35]
    b = sorted(nums)[49]
    return nums[nums.index(b) - 1] if a < b else None
