
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)+1):
            sublist = my_list[i:j]
            if len(sublist) > 0 and np.prod(sublist) == -81:
                result.append(sublist)
    return result
