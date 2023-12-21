
def lists_with_product_equal_n(circular_list):
    len_l = len(circular_list)
    circular_list += circular_list
    res = []
    for i in range(len_l):
        for j in range(i+1, i+len_l+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -91:
                res.append(sublist)
    return res
