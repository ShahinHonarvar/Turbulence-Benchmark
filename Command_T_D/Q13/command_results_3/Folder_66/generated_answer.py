
def find_second_largest_num(nums):
    return nums[nums.index(sorted(set(nums))[-2]) - 50:nums.index(sorted(set(nums))[-1]) + 2]
