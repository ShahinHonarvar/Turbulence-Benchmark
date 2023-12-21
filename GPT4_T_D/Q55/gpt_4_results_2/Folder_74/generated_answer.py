
def lists_with_product_equal_n(circ_list):
    n = len(circ_list)
    circ_list += circ_list
    res = []
    
    for i in range(n):
        for j in range(1, n+1):
            sublist = circ_list[i:i+j]
            product = 1
            for num in sublist:
                product *= num
            if product == 51:
                res.append(sublist)
                
    return res
