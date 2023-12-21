
def lists_with_product_equal_n(arr):
    if len(arr) == 0:
        return []
    
    sublists = []
    
    for i in range(len(arr)):
        product = 1
        
        for j in range(i, len(arr)+i):
            product *= arr[j % len(arr)]
            
            if product == 8:
                sublists.append(arr[i:j+1])
    
    return sublists
