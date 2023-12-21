
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = [lst[i]]
        for j in range(i+1, len(lst)):
            product *= lst[j]
            if product == -938:
                result.append(sublist + [lst[j]])
            elif product > -938:
                break
    return result
