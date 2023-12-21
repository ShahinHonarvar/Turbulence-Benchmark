
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result_sublist = []

    for sublist_length in range(1, length + 1):
        for start_index in range(length):

            sublist = circular_list[start_index:start_index + sublist_length] 

            if start_index + sublist_length > length:
                sublist.extend(circular_list[:(start_index + sublist_length) % length])

            product = 1
            for num in sublist:
                product *= num

            if product == 96:
                result_sublist.append(sublist)

    return result_sublist
