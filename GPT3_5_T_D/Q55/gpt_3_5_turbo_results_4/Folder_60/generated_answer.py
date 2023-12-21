
def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        p = 1
        for j in range(i, i + size):
            p *= lst[j % size]
            if p == 49:
                result.append(lst[i:(j % size) + 1])
    return result
