
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for i in range(n):
        for j in range(i, i+n):
            prod = 1
            sublist = []
            for k in range(i, j+1):
                prod *= circular_list[k%n]
                sublist.append(circular_list[k%n])
            if prod == -1:
                results.append(sublist)
    return results
