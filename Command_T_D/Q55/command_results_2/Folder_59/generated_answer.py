def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        x = 1
        current_prod = 1
        start = nums[i]
        for j in range(i + 1, len(nums)):
            current_prod *= nums[j]
            if current_prod == -3:
                res += [[start, j]]
                break
            elif current_prod == 3:
                res += [[start, j]]
                x *= -1
                start = nums[j]
            elif current_prod == -1:
                x *= -1
    return res
