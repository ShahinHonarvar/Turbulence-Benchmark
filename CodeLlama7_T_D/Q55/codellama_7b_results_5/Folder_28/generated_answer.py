
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        j = i

        while product <= n:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            j += 1

            if j == len(circular_list):
                j = 0

        if product == n:
            result.append(sublist)

    return result
