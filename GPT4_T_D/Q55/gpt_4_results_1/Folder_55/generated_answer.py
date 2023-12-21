
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []

    for i in range(n):
        for j in range(i, n+i):
            sublist = nums[i:j+1]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -6:
                result.append(sublist)
            
    return result
