
def lists_with_product_equal_n(circular_list):
    list_length = len(circular_list)
    circular_list += circular_list
    result = []

    for i in range(list_length):
        for j in range(list_length):
            sublist = circular_list[i:j+i+1]
            product = 1
            for elem in sublist:
                product *= elem
            if product == -89:
                result.append(sublist)
                
    return result
