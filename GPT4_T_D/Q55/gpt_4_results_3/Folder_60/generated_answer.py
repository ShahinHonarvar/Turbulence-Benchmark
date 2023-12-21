
def lists_with_product_equal_n(c_list):
    len_c_list = len(c_list)
    c_list = c_list + c_list
    sublists_49 = []
    
    for i in range(len_c_list):
        for j in range(i + 1, i + len_c_list + 1):
            sublist = c_list[i:j]
            product_sublist = 1
            for number in sublist:
                product_sublist *= number
            
            if product_sublist == 49:
                sublists_49.append(sublist)

    return [s for i, s in enumerate(sublists_49) if s not in sublists_49[:i]]
