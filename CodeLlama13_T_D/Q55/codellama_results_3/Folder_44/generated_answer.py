
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublist = [lst[i]]
        product = lst[i]
        for j in range(i+1, len(lst)):
            product *= lst[j]
            if product == n:
                sublist.append(lst[j])
                result.append(sublist)
    return result
