
def find_second_largest_num(nums):
    return nums[nums.index(sorted(set(nums))[-2])-1] if len(set(nums))>1 else None
