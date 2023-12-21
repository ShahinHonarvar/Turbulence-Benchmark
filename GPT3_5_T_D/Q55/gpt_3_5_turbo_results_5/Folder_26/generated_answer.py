
def lists_with_product_equal_n(values):
    n = len(values)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(i, i+n):
            product *= values[j % n]
            if product == 93:
                sublist = values[i:j % n + 1]
                result.append(sublist)
    
    return result
