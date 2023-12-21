
def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    circular_list += circular_list
    res = []
    
    for i in range(size):
        for j in range(i+1, size + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            
            if product == 415:
                res.append(sublist)
                
    return res
