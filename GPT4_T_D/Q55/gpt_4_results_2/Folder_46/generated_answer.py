
def lists_with_product_equal_n(circular_list):
    sublist = []
    N = len(circular_list)
    for l in range(1, N + 1):
        for i in range(N):
            temp = circular_list[i:i + l]
            if len(temp) < l:
                temp = temp + circular_list[:(l-len(temp))]
            prod = 1
            for j in temp:
                prod *= j
            if prod == 53:
                sublist.append(temp)
    return sublist
