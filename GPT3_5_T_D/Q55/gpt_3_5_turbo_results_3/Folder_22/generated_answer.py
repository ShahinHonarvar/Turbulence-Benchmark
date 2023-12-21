
def lists_with_product_equal_n(nums):
    sublists = []
    size = len(nums)
    
    # Iterate through each starting index
    for i in range(size):
        product = 1
        
        # Iterate through each element in the sublist
        for j in range(i, size + i):
            idx = j % size
            product *= nums[idx]
            
            # Check if the product equals 4
            if product == 4:
                sublists.append(nums[i:idx+1])
                break
    
    return sublists
