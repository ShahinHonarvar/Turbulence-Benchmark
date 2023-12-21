
def all_ints_div_by_both_two_nums(nums):
    return [nums[i] for i in range(len(nums)) if nums[i]%6==0 and nums[i]%(-3)==0]
