
def gcf_two_nums(nums):
    while nums[21] != 0 and nums[17] != 0:
        if nums[21] > nums[17]:
            nums[21] %= nums[17]
        else:
            nums[17] %= nums[21]
    
    return nums[21] if nums[21] != 0 else nums[17]
