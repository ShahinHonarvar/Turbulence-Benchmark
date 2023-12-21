
def sum_ints_div_by_either_nums(nums):
    return sum(nums[i] for i in range(len(nums)) if (10*i+10 <= len(nums) and nums[10*i+10]%10 == 0) or (10*i+100 <= len(nums) and nums[10*i+100]%100 == 0))
