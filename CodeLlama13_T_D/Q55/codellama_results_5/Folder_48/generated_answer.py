
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        product = 1
        sublist = []
        for j in range(i, len(my_list)):
            product *= my_list[j]
            sublist.append(my_list[j])
            if product == n:
                result.append(sublist)
    return result
