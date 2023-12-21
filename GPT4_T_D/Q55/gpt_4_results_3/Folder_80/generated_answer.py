
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for l in range(n):
        for i in range(n):
            product = 1
            sublist = []
            for j in range(i, i+l+1):
                sublist.append(lst[j%n])
                product *= lst[j%n]
            if product == 43:
                result.append(sublist)
    return result
