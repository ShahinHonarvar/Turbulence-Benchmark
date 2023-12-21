
def lists_with_product_equal_n(circ_list):
    num_elems = len(circ_list)
    result = []
    for sublist_len in range(1, num_elems + 1):
        for start_index in range(num_elems):
            sublist = [circ_list[(start_index + i) % num_elems] for i in range(sublist_len)]
            product = 1
            for num in sublist:
                product *= num
            if product == -57:
                result.append(sublist)
    return result
