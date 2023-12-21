
def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        sublist = []
        product = 1
        for j in range(n):
            index = (i + j) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -44:
                sublists.append(sublist.copy())
                break
    return sublists
