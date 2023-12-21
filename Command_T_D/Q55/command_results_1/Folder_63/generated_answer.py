def lists_with_product_equal_n(nums):
    result = []
    for j in range(len(nums) - 1):
        i = j
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1
        if i == len(nums) - 1:
            continue
        prod = 1
        for k in range(i, len(nums)):
            prod *= nums[k]
        if prod == 96:
            result.append(nums[i:k + 1])
    return result
