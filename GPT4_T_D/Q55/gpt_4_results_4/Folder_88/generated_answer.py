
def lists_with_product_equal_n(nums):
    n = len(nums)
    results = []

    for i in range(n):
        for j in range(i, i + n):
            sublist = nums[i:j] if j < n else nums[i:] + nums[:j%n]
            product = 1
            for num in sublist:
                product *= num
            if product == -56:
                results.append(sublist)
    return results
