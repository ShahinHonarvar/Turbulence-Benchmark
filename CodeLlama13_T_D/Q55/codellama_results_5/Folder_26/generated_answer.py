
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = [lst[i]]
        j = (i + 1) % len(lst)
        while j != i and product * lst[j] != 93:
            product *= lst[j]
            sublist.append(lst[j])
            j = (j + 1) % len(lst)
        if product == 93:
            result.append(sublist)
    return result
