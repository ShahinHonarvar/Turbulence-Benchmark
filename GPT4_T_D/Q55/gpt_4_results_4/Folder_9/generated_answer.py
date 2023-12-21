
def lists_with_product_equal_n(circular_list):
    len_l = len(circular_list)
    circular_list = circular_list + circular_list
    res = []
    for sub_len in range(1, len_l + 1):
        for start in range(len_l):
            sublist = circular_list[start:start+sub_len]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -36:
                res.append(sublist)
    return res
