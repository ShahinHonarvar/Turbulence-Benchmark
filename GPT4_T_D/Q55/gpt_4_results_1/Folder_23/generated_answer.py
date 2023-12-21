
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    matching_sublists = []
    for start_index in range(length):
        for end_index in range(start_index, length):
            product = 1
            for i in range(start_index, end_index + 1):
                product *= circular_list[i % length]
            if product == -95:
                matching_sublists.append(circular_list[start_index:end_index + 1])
    return matching_sublists
