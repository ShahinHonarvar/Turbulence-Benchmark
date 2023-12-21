
def find_second_smallest_num(nums):
    nums = sorted(nums)
    for i in range(22, 89):
        if nums[i-1] != nums[i]:
            return nums[i]
    return None
