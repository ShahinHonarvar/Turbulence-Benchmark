
def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []
    for i in range(length):
        p = 1
        sublist = []
        for j in range(i, i + length):
            p *= lst[j % length]
            sublist.append(lst[j % length])
            if p == -8:
                result.append(sublist.copy())
            if p == 0:
                break
    return result
