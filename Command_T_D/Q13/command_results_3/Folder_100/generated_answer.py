
def find_second_largest_num(nums):
    return nums[nums.index(sorted(set(nums)[-2])][:42] + nums[nums.index(sorted(set(nums)[-2])][68:])]
