
def lists_with_product_equal_n(nums):
    n = len(nums)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, i+n):
            product *= nums[j % n]
            if product == -23:
                sublists.append(nums[i:j+1])
    return sublists
