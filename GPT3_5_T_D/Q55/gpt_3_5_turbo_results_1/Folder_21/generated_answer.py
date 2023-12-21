
def lists_with_product_equal_n(nums):
    target = 851
    n = len(nums)
    sublists = []
    
    for i in range(n):
        product = 1
        for j in range(i, n+i):
            product *= nums[j % n]
            if product == target:
                sublists.append(nums[i:j % n+1])
    
    return sublists
