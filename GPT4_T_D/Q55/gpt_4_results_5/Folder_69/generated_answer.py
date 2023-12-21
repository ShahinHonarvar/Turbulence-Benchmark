
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= circular_list[j]
            if product == 90:
                sublists.append(circular_list[i: j+1])
            elif product > 90:
                break
        if i != 0 and product == 90:
            j = 0
            while product == 90:
                product = product // circular_list[j - 1] * circular_list[(i + j) % n]
                if product == 90:
                    sublists.append(circular_list[j: i + j + 1])
                j += 1

    return sublists
