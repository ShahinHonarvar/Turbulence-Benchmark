
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        prod = 1
        sublist = []
        for j in range(i, len(my_list)):
            prod *= my_list[j]
            sublist.append(my_list[j])
            if prod == 40:
                result.append(sublist)
                break
    return result
