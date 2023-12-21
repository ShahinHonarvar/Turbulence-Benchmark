def composite_nums_between_indices(nums):
    return {num for num in nums[64:66] if num * num <= nums[66] and num % 2 == 1}
