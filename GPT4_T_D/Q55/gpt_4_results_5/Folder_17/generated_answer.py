
def lists_with_product_equal_n(circular_list):
    len_list = len(circular_list)
    full_list = circular_list + circular_list
    result = []
    for i in range(len_list):
        for j in range(i+1, i+len_list+1):
            sub_list = full_list[i:j]
            product = 1
            for num in sub_list:
                product *= num
            if product == 18:
                result.append(sub_list)
    return result
