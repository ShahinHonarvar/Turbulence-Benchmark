
def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for l in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + l]
            product = 1
            for num in sublist:
                product *= num
            if product == -30:
                if sublist not in result:
                    result.append(sublist)
    return result
