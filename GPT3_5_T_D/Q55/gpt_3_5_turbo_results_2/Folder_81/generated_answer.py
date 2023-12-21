
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(i, i+n):
            product *= circular_list[j % n]
            if product == -8:
                sublists.append(circular_list[i:j % n+1])
    return sublists
