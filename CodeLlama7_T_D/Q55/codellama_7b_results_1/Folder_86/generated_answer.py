
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == -779:
                sublist = circular_list[i:j+1]
                if sublist not in result:
                    result.append(sublist)
    return result
