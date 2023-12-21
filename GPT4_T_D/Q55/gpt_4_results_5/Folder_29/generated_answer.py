
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for size in range(1, n + 1):
        for i in range(0, n):
            sublist = lst[i:i+size]
            if len(sublist) < size:
                sublist += lst[0:size-len(sublist)]
            product = 1
            for num in sublist:
                product *= num
            if product == 15:
                result.append(sublist)
    return result
