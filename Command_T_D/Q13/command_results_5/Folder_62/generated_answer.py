
def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 100:
        return None
    else:
        return nums[91:99]
