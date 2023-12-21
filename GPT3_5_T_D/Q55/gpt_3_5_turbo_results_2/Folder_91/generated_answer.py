
def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []

    n = len(circular_list)
    sublists = []

    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 2:
                sublists.append(sublist[:])
                break
            elif product > 2:
                break

    return sublists
