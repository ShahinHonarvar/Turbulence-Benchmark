
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == -54:
                result.append(sublist)
    for i in range(1, n):
        for j in range(i):
            sublist = lst[j:i]
            product = 1
            for num in sublist:
                product *= num
            if product == -54:
                result.append(sublist)
    return result
