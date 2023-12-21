def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    else:
        return nums[25:87][-2]
