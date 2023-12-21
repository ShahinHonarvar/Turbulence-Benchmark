
def lists_with_product_equal_n(circle):
    def product(arr):
        p = 1
        for num in arr:
            p *= num
        return p
    
    n = len(circle)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = circle[i:j+1] + circle[j+1:] + circle[:i]
            if product(sublist) == 93:
                result.append(sublist)
    
    return result
