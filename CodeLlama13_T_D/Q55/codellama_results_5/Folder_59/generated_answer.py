
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        product = 1
        sublist = []
        for j in range(i, len(my_list)):
            product *= my_list[j]
            if product == -3:
                sublist.append(my_list[j])
                result.append(sublist)
                break
    return result
