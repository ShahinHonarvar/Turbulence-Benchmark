
def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= lst[j % length]
            if product == 632:
                result.append(lst[i:j % length + 1])
    
    return result
