
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    if length == 0:
        return []

    result = []
    circular_list = circular_list + circular_list

    for i in range(length):
        for j in range(i+1, i+length+1):
            sublist = circular_list[i:j]
            product = 1
            for x in sublist:
                product *= x
            if product == -6:
                result.append(sublist)
    return result
