def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[29])+30:200].index(min(nums[nums.index(sorted(nums)[29])+30:200]))+1)
