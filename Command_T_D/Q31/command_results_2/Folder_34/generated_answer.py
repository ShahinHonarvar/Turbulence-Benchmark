def if_perfect_num(nums):
    return nums[97] == sum(nums[:97]) == sum(nums[97+1:])
