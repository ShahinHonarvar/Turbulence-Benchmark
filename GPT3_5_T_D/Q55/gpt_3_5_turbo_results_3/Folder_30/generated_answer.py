
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    product_dict = {}

    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= circular_list[j % length]
            if product == 99:
                sublist = circular_list[i:j+1]
                if sublist not in result:
                    result.append(sublist)
                break

    return result
