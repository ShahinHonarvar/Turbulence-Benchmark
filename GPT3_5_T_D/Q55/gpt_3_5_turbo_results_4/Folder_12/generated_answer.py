
def lists_with_product_equal_n(nums):
    n = len(nums)
    results = []
    
    def product_equal_n(start, end):
        product = 1
        sublist = []
        for i in range(start, end):
            product *= nums[i]
            sublist.append(nums[i])
        if product == -18:
            results.append(sublist)

    for i in range(n):
        for j in range(i+1, n+1):
            product_equal_n(i, j)
    
    return results
