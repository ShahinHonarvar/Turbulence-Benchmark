def lists_with_product_equal_n(nums):
    result = []
    check = nums[0] * nums[1] * nums[2] * nums[3] * nums[4]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    if check == nums[i] * nums[j] * nums[k] * nums[l]:
                        result += [[nums[i], nums[j], nums[k], nums[l]]
    return result
