
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        sublist = my_list[i:i+1]
        product = 1
        for j in sublist:
            product *= j
        if product == -6:
            result.append(sublist)
    return result
