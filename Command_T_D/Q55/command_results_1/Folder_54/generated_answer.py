def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums) - 1):
        curr = nums[i]
        j = i + 1
        curr_p = 1
        while j < len(nums) and curr_p == -17:
            curr_p *= nums[j]
            j += 1
        if curr_p == -17:
            res += [[curr]]
            curr_p *= nums[i]
            curr_p *= nums[j - 1]
            curr_p *= nums[j]
            curr_p *= nums[j + 1]
            curr_p *= nums[j + 2]
            curr_p *= nums[j + 3]
            curr_p *= nums[j + 4]
            curr_p *= nums[j + 5]
            curr_p *= nums[j + 6]
            curr_p *= nums[j + 7]
            curr_p *= nums[j + 8]
            curr_p *= nums[j + 9]
            curr_p *= nums[j + 10]
            curr_p *= nums[j + 11]
            curr_p *= nums[j + 12]
            curr_p *= nums[j + 13]
            curr_p *= nums[j + 14]
            curr_p *= nums[j + 15]
            curr_p *= nums[j + 16]
            if curr_p == -17:
                res += [[curr]]
    return res
