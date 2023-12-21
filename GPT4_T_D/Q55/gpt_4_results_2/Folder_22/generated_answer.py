
def lists_with_product_equal_n(int_list):
    sublist = []
    for i in range(len(int_list)):
        for j in range(i, len(int_list)):
            if j == len(int_list) - 1:
                temp_sublist = int_list[i:j+1] + [int_list[0]]
            else:
                temp_sublist = int_list[i:j+1]
            if prod(temp_sublist) == 4:
                sublist.append(temp_sublist)
    return sublist

def prod(a_list):
    p = 1
    for i in a_list:
        p *= i
    return p
