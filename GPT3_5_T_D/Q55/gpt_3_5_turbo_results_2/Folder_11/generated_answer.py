
def lists_with_product_equal_n(nums):
    results = []
    n = len(nums)

    def product_equal_n(start, end):
        if start == end:
            return []
        product = 1
        for i in range(start, end):
            product *= nums[i]
        if product == -15:
            return nums[start:end]
        return []

    for i in range(n):
        for j in range(i, n + i):
            results.append(product_equal_n(i, j))

    return [x for x in results if x]
