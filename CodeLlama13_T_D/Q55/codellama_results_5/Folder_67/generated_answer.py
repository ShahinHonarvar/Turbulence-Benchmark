
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:i+1]
        product = 1
        while product < 33 and len(sublist) <= len(circular_list):
            product *= sublist[-1]
            sublist.append(sublist[-1])
        if product == 33:
            result.append(sublist)
    return result
