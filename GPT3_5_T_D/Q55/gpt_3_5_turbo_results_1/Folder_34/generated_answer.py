
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    
    for size in range(1, n+1):
        for i in range(n):
            sublist = nums[i:min(i+size, n)] + nums[:max(i+size-n, 0)]
            if sublist and reduce(lambda x, y: x*y, sublist) == -81:
                result.append(sublist)
    
    return result
