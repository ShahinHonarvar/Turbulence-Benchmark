
def lists_with_product_equal_n(nums):
    sublists = []
    n = len(nums)
    product = 1

    for i in range(n):
        for j in range(i, i + n):
            product *= nums[j % n]
            if product == -690:
                sublists.append(nums[i:j % n + 1])
    
    return sublists
