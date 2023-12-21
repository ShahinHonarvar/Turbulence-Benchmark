
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    res = []
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j+1):
                prod *= circular_list[k]
            if prod == 0:
                res.append(circular_list[i:j+1])
    for i in range(n):
        for j in range(i):
            prod = 1
            for k in range(i, n):
                prod *= circular_list[k]
            for k in range(j+1):
                prod *= circular_list[k]
            if prod == 0:
                res.append(circular_list[i:n] + circular_list[0:j+1])
    return res
