
def lists_with_product_equal_n(circular_list):
    list_len = len(circular_list)
    circular_list += circular_list
    result = []

    for start_index in range(list_len):
        for sublist_len in range(1, list_len + 1):
            sublist = circular_list[start_index:start_index + sublist_len]
            product = 1
            for number in sublist:
                product *= number
            if product == -26:
                if sublist not in result:
                    result.append(sublist)

    return result
