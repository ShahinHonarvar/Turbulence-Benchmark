
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] * nums[j] == -3:
                result.append(nums[i:j+1])
    return result
