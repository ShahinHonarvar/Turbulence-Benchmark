
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:i+1]
        product = 1
        for j in range(i, len(sublist)):
            product *= sublist[j]
            if product == 100:
                result.append(sublist)
                break
    return result
