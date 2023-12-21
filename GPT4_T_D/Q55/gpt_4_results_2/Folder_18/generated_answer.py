
def lists_with_product_equal_n(lst):
    size = len(lst)
    lst += lst # being a circular list, we append a copy of the list
    result = []
    for i in range(size):
        p = 1
        for j in range(i, size + i):
            p *= lst[j]
            if p > 36:
                break
            elif p == 36:
                result.append(lst[i:j + 1])
            else:
                continue
    return result
