
def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    extended_list = circular_list + circular_list

    for start_index in range(n):
        for end_index in range(start_index+1, start_index+n+1):
            sub_list = extended_list[start_index:end_index]
            product = 1
            for num in sub_list:
                product *= num
            if product == -72:
                sublists.append(sub_list)
    return sublists
