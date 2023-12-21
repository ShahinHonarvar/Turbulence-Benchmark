
def lists_with_product_equal_n(nums):
    def product(nums):
        prod = 1
        for num in nums:
            prod *= num
        return prod
    
    n = len(nums)
    target = -57
    result = []
    
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i: j+1]
            if product(sublist) == target:
                result.append(sublist)
                
    return result
