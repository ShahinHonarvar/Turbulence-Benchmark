
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == -26:
                result.append(sublist)
        sublist = lst[i:] + lst[:i]
        product = 1
        for num in sublist:
            product *= num
        if product == -26:
            result.append(sublist)
    return result
