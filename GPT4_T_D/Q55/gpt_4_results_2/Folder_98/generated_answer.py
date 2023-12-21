
def lists_with_product_equal_n(circular_list):
    len_circular_list = len(circular_list)
    circular_list.extend(circular_list)
    result = []
    for i in range(len_circular_list):
        for j in range(i+1, i+len_circular_list+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -1:
                result.append(sublist)
    return result
