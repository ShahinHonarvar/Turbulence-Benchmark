
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = [lst[i]]
        for j in range(i+1, len(lst)):
            product *= lst[j]
            if product == -18:
                result.append(sublist + [lst[j]])
                break
        else:
            continue
    return result
