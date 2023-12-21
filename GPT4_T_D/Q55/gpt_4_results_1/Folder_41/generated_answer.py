
def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    circular_list = circular_list * 2
    result = []
    for i in range(len_list):
        for j in range(i+1, i+len_list+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -20:
                result.append(sublist)
    return result
