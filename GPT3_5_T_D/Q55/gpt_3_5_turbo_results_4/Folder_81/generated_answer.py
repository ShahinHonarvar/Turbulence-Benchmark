
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 0
    
    for i in range(n):
        for j in range(i, i+n):
            product = product * lst[j % n] if product != 0 else lst[j % n]
            if product == -8:
                result.append(lst[i:j % n + 1])
    
    return result
