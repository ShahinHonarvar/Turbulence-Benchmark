def gcf_two_nums(nums):
    return next(x for x in range(min(nums),0,-1) if all(x%y==0 for y in nums))
