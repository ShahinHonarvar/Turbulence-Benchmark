
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            index = j % size
            product *= lst[index]
            if product == -20:
                result.append(lst[i:j+1])
    return result
