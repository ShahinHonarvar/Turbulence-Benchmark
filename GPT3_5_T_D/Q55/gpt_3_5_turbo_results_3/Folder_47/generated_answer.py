
def lists_with_product_equal_n(lst):
    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    
    result = []
    n = len(lst)
    
    for i in range(n):
        for j in range(i+1, n+1):
            if product_of_sublist(lst[i:j]) == -94:
                result.append(lst[i:j])
    
    return result
