
def lists_with_product_equal_n(nums):
    n = len(nums)
    if n == 0:
        return []
    result = []
    for i in range(n):
        for j in range(i, i + n):
            sublist = nums[i:(j % n) + 1] if j < n else nums[i:] + nums[:(j % n) + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -32:
                result.append(sublist)
    return result
