
def lists_with_product_equal_n(lst):
    n = len(lst)
    lst_extended = lst * 2
    results = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = lst_extended[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -94:
                results.append(sublist)
    return results
