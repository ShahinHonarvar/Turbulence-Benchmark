
def lists_with_product_equal_n(circ_list):
    results = []
    m = len(circ_list)
    if m == 0: return []
    
    circ_list = circ_list + circ_list

    for l in range(1,m+1):
        for i in range(m):
            sublist = circ_list[i:i+l]
            product = 1
            for item in sublist:
                product *= item
            if product == 57:
                results.append(sublist)
    return results
