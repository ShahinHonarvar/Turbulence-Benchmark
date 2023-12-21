
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:i+1]
        product = 1
        for j in range(len(sublist)):
            product *= sublist[j]
            if product == 247:
                result.append(sublist)
    return result
