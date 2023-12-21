
def lists_with_product_equal_n(l):
    result = []
    size = len(l)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = l[i:j] if j < size else l[i:] + l[:j-size]
            product = 1
            for num in sublist:
                product *= num
            if product == -75:    
                result.append(sublist)            
    return result
