def find_second_smallest_num(nums):
    secondSmallest = sorted(nums)[62]
    if secondSmallest < len(nums) - 1:
        return nums[secondSmallest + 1]
    else:
        return None
