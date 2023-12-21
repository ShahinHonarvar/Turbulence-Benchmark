
def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    else:
        subset_nums = nums[82:87]
        subset_nums.sort()
        return subset_nums[1]
