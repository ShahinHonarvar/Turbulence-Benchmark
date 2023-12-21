
def find_second_largest_num(nums):
    maxnum = max(nums)
    for i in range(len(nums)):
        if i == 0:
            continue
        elif i == len(nums) - 1:
            continue
        elif nums[i] > maxnum:
            return nums[i]
        elif nums[i] == maxnum:
            return nums[i]
    return None
