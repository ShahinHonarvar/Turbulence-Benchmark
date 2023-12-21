import itertools
def all_odd_ints_exclusive(nums):
    idx = next((i for i,x in enumerate(nums) if x%2==1), -1)
    if idx==-1:
        return []
    else:
        return [x for x in nums[idx+1:70]]
