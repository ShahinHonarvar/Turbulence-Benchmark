
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list.extend(circular_list[:n-1])
    res = []
    
    for i in range(n):
        for j in range(i+1, i+n):
            sublist = circular_list[i:j+1]
            product = 1
            for num in sublist:
                product *= num
                
            if product == -81:
                res.append(sublist)
                
    return res
