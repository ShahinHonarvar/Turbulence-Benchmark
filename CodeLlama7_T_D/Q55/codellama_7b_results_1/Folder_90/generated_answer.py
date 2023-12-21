
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        while product != -690:
            product *= circular_list[i]
            sublist.append(circular_list[i])
            i += 1

        result.append(sublist)

    return result
