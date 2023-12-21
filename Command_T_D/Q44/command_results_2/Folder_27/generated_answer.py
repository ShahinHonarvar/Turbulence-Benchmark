def composite_nums_between_indices(nums):
    return {num for num in nums[22:63] if num % 2 == 1 and any(num % i == 0 for i in range(3, int(num ** .5) + 1, 2))}
