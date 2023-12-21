
def lists_with_product_equal_n(lst):
    results = []
    length = len(lst)
    
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= lst[j % length]
            if product == -906:
                results.append(lst[i:(j % length) + 1])
    
    return results
