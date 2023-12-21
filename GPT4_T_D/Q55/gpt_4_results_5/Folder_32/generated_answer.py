
def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    sublists = []
    for i in range(len_list):
        for j in range(i+1,len_list+1):
            for k in range(j+1,len_list+2):
                if k<=len_list:
                    sublist = circular_list[i:j]+circular_list[:k]
                else:
                    sublist = circular_list[i:j]
                prod = 1
                for x in sublist:
                    prod *= x
                if prod == 76:
                    if sublist not in sublists:
                        sublists.append(sublist)   
    return sublists
