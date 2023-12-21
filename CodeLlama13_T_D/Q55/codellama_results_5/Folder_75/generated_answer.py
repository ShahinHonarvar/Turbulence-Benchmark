
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = [lst[i]]
        j = (i + 1) % len(lst)
        while j != i:
            product *= lst[j]
            if product == n:
                result.append(sublist)
            elif product > n:
                break
            else:
                sublist.append(lst[j])
            j = (j + 1) % len(lst)
    return result
