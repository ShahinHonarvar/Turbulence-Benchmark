
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = [lst[i]]
        for j in range(i+1, len(lst)):
            prod *= lst[j]
            if prod == -51:
                result.append(sublist + [lst[j]])
                break
            elif prod > -51:
                break
            else:
                sublist.append(lst[j])
    return result
