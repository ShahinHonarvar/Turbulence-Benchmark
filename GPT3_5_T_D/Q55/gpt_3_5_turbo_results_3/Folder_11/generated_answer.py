
def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    
    for i in range(length):
        sublists = []
        product = 1
        
        for j in range(i, i + length):
            index = j % length
            product *= lst[index]
            
            if product == -15:
                sublists.append(lst[i:index + 1])
                
        result.extend(sublists)
        
    return result
