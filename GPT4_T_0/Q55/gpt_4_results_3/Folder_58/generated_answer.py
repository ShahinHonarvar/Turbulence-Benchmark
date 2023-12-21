
def lists_with_product_equal_n(lst):
    n = 733
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
        sublist = lst[i:] + lst[:i]
        product = 1
        for num in sublist:
            product *= num
        if product == n:
            result.append(sublist)
    return result
