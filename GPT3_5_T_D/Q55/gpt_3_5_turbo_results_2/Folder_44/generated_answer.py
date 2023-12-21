
def lists_with_product_equal_n(lst):
    n = 29
    result = []
    size = len(lst)
    
    for i in range(size):
        product = 1
        for j in range(i, size):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j+1])
            elif product > n:
                break
    
    return result
