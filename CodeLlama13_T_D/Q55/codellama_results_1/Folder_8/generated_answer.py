
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = [lst[i]]
        for j in range(i+1, len(lst)):
            prod *= lst[j]
            if prod == -41:
                result.append(sublist)
                break
            elif prod > -41:
                break
            else:
                sublist.append(lst[j])
    return result
