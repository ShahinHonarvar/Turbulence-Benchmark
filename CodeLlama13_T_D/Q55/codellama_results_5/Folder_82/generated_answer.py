
def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = [lst[i]]
        for j in range(i+1, len(lst)):
            prod *= lst[j]
            if prod == n:
                result.append(sublist + [lst[j]])
        if prod != n and len(sublist) > 1:
            result.append(sublist)
    return result
