
def lists_with_product_equal_n(nums):
    sublists = []
    length = len(nums)
    product = 1
    
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= nums[j % length]
            if product == 6:
                sublists.append(nums[i: (j % length) + 1])
            
    return sublists
