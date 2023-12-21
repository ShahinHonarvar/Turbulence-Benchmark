
def lists_with_product_equal_n(lst):
    def product(arr):
        prod = 1
        for num in arr:
            prod *= num
        return prod
    
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n+i):
            sublist = lst[i:j+1]
            if product(sublist) == 48:
                result.append(sublist)
    
    return result
