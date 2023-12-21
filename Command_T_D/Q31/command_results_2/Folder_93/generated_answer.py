def if_perfect_num(nums):
    return nums[45] == sum(nums[0:45]) == sum(nums[45+1:])
