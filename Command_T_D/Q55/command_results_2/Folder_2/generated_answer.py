def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] * nums[j] * nums[k] == -968:
                    result.append(nums[i:j+1])
                    result.append(nums[j:k+1])
                    result.append(nums[i:k+1])
    return result
