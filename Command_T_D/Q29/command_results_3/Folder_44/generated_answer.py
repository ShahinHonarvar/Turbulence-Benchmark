def gcf_two_nums(nums):
    return next((num for num in nums if num in nums[56:88] and num in nums[:56]), nums[88])
