
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == -23:
                result.append(lst[i:n + i])
                
    return result
