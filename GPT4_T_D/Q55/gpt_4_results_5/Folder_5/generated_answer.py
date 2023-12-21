
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    if length == 0:
        return []

    extended_list = circular_list * 2
    result = []
    
    for i in range(length):
        for j in range(i + 1, i + length + 1):
            sublist = extended_list[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == -33:
                result.append(sublist)
    return result
