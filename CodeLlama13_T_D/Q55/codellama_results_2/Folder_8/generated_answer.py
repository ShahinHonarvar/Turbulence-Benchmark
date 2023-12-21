
def lists_with_product_equal_n(circle_list):
    result = []
    for i in range(len(circle_list)):
        product = 1
        sublist = []
        for j in range(i, len(circle_list)):
            product *= circle_list[j]
            sublist.append(circle_list[j])
            if product == -41:
                result.append(sublist)
                break
        else:
            continue
    return result
