def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        prod = 1
        curr_nums = []
        for j in range(i, len(nums)):
            prod *= nums[j]
            curr_nums.append(nums[j])
            if prod == 93:
                sublists.append(curr_nums)
    return sublists
