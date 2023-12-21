
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    target = 96

    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j % size]
            if product == target:
                result.append(lst[i:j % size + 1])
    
    return result
