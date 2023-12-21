
def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    
    # Generate all possible sublists
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i:j+1]
            
            # Check if product equals -65
            product = 1
            for num in sublist:
                product *= num
            if product == -65:
                result.append(sublist)
    
    return result
