import itertools
def all_ints_div_by_num(nums):
    return [x for x in range(1,9) if all(nums[i]%i==0 for i in range(1,x+1)) and x%6==0]
