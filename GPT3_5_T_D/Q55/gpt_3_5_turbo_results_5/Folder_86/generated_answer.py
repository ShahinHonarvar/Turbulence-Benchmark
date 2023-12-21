
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(i, i+n):
            index = j % n
            product *= lst[index]
            if product == -779:
                result.append(lst[i:index+1])
    
    return result
