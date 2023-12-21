
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)
    product = 1
    
    for i in range(size):
        product = nums[i]
        
        if product == -22:
            result.append([nums[i]])
        
        for j in range(i+1, size * 2):
            if product * nums[j % size] == -22:
                sublist = nums[i:j % size + 1]
                if sublist not in result:
                    result.append(sublist)
                
    return result
