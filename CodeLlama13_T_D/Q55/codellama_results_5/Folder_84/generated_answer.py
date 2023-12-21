
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = [circular_list[i]]
        for j in range(i+1, len(circular_list)):
            product *= circular_list[j]
            if product == -906:
                result.append(sublist)
            elif product > -906:
                break
            else:
                sublist.append(circular_list[j])
    return result
