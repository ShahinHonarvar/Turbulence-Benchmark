
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    
    def is_product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -10
    
    for i in range(n):
        for j in range(i, n + i):
            sub = lst[i:j+1]
            if is_product_equal_n(sub):
                result.append(sub)
    
    return result
