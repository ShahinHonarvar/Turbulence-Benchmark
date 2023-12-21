 
def lists_with_product_equal_n(nums):
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] * nums[j] == 13:
                yield [nums[i]] + nums[i+1:j] + [nums[j]]
    if len(nums) >= 2:
        yield [nums[0]] + nums[1:] + [nums[-1]]
