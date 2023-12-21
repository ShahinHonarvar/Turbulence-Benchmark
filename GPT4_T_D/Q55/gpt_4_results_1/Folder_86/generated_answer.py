
def lists_with_product_equal_n(lst):
    n = len(lst)
    results = []
    for i in range(n):
        for j in range(i, n+i):
            sublist = lst[i:j % n] if j >= n else lst[i:j+1] 
            product = 1
            for num in sublist:
                product *= num
            if product == -779:
                results.append(sublist)
    return results
