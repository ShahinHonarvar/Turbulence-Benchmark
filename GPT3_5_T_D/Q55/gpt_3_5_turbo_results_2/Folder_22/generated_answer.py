
def lists_with_product_equal_n(circle):
    result = []
    size = len(circle)

    for i in range(size):
        product = 1
        j = i
        sublist = []
        
        while product != 0:
            sublist.append(circle[j])
            product *= circle[j]
            
            if product == 4:
                result.append(sublist[:])
            
            j = (j + 1) % size
            
            if j == i:
                break
    
    return result
