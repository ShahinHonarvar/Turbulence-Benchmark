
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    
    for i in range(n):
        product = 1
        for j in range(1, n+1):
            index = (i + j - 1) % n
            product *= nums[index]
            
            if product == 990:
                sublist = nums[i:index+1]
                result.append(sublist)
    
    return result
