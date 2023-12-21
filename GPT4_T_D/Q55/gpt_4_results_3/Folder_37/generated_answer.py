
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for l in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i+l]
            if len(sublist) < l:
                sublist.extend(lst[:l - len(sublist)])
            product = 1
            for num in sublist:
                product *= num
            if product == -76:
                result.append(sublist)
    return result
