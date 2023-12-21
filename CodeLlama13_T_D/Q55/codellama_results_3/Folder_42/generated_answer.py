
def lists_with_product_equal_n(my_list):
    result = []
    for i in range(len(my_list)):
        prod = 1
        sublist = [my_list[i]]
        j = i + 1
        while j < len(my_list) and prod * my_list[j] == 25:
            prod *= my_list[j]
            sublist.append(my_list[j])
            j += 1
        if prod == 25:
            result.append(sublist)
    return result
