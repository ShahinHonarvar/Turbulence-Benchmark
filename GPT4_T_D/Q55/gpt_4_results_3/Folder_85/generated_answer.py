
def lists_with_product_equal_n(circular_list):
    results = []
    n = len(circular_list)
    circular_list.extend(circular_list)
    for i in range(n):
        for j in range(i+1, i+n+1):
            prod = 1
            for k in range(i, j):
                prod *= circular_list[k]
            if prod == -97:
                results.append(circular_list[i:j])
    return results
