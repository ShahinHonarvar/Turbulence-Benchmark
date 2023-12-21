
def lists_with_product_equal_n(circular_list):
    n = 15
    result = []
    list_len = len(circular_list)
    extended_list = circular_list * 2

    for sublist_len in range(1, list_len + 1):
        for start_index in range(0, list_len):
            sublist = extended_list[start_index: start_index + sublist_len]
            product = 1
            for elem in sublist:
                product *= elem
                if product == n:
                    result.append(sublist)
                elif product > n: 
                    break
    return result
