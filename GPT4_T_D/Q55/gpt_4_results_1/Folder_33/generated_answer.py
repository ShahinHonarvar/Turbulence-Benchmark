
def lists_with_product_equal_n(circular_list):
    from numpy import prod
    n = len(circular_list)
    results = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            if prod(circular_list[i:j%n]) == -115:
                results.append(circular_list[i:j%n])
    return results
