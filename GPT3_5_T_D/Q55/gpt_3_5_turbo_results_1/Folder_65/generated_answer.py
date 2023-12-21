
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(i, i+n):
            product *= lst[j % n]
            if product == 46:
                result.append(lst[i:j+1])
    
    return result
