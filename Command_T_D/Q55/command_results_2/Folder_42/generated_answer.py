def lists_with_product_equal_n(nums):
    result = []
    for start in range(1, len(nums) + 1):
        for end in range(start, len(nums) + 1):
            for j in range(start, end):
                nums[j] = 25
            if nums == [25] * (end - start):
                result += [[25] + nums[start:end]]
    return result
