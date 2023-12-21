
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= lst[(i+j) % size]
            if product == -779:
                result.append(lst[i:i+j+1])
    return result
