
def lists_with_product_equal_n(lst):
    results = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, i+size):
            index = j % size
            product *= lst[index]
            if product == -33:
                results.append(lst[i:j+1])
    return results
