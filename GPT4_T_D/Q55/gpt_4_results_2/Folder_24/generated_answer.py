
def lists_with_product_equal_n(circular_list):
    result = []
    size = len(circular_list)
    extended_list = circular_list + circular_list
    for i in range(size):
        for j in range(i + 1, i + size + 1):
            sublist = extended_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -89:
                result.append(sublist)
    return result
