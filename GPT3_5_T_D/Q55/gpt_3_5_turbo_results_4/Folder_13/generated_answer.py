
def lists_with_product_equal_n(nums):
    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    
    result = []
    size = len(nums)
    
    for i in range(size):
        for j in range(i, size+i):
            if product_of_sublist(nums[i:j+1]) == 54:
                result.append(nums[i:j+1])
    
    return result
