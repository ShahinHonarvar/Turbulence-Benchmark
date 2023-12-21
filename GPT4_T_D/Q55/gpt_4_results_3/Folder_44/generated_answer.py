
def lists_with_product_equal_n(lst):
    length = len(lst)
    result = []
    for i in range(length):
        product = lst[i]
        if product == 29:
            result.append([product])
        for j in range(i+1, length):
            product *= lst[j]
            if product == 29:
                result.append(lst[i:j+1])
        if i != 0:
            product *= lst[0]
            if product == 29:
                result.append(lst[i:] + [lst[0]])
            for j in range(1, i):
                product *= lst[j]
                if product == 29:
                    result.append(lst[i:] + lst[:j+1])
    return result
