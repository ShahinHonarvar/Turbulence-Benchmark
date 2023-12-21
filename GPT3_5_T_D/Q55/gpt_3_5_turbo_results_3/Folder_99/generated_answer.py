
def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        prod = 1
        for j in range(i, i+len(nums)):
            prod *= nums[j%len(nums)]
            if prod == 415:
                sublists.append(nums[i: (j%len(nums))+1])
    return sublists
