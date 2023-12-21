
def lists_with_product_equal_n(lst):
    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1]
            if product(sublist) == -9:
                result.append(sublist)
                
    return result
