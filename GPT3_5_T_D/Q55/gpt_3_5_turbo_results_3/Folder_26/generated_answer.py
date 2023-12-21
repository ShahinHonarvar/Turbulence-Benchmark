
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)
    
    for i in range(size):
        product = 1
        sublist = []
        
        for j in range(i, i + size):
            product *= nums[j % size]
            sublist.append(nums[j % size])
            
            if product == 93:
                result.append(sublist[:])
                break
        
    return result
