
def lists_with_product_equal_n(circular_list):
    result = []
    if len(circular_list) == 0:
        return result

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    for i in range(len(circular_list)):
        sublist = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            sublist.append(circular_list[index])
            if product_of_sublist(sublist) == 15:
                result.append(sublist[:])
    
    return result
