
def lists_with_product_equal_n(circular_list):
    valid_sublists = []

    for start_index in range(len(circular_list)):
        for sublist_size in range(1, len(circular_list) + 1):
            sublist = []
            product = 1
            for offset in range(sublist_size):
                actual_index = (start_index + offset) % len(circular_list)
                sublist.append(circular_list[actual_index])
                product *= circular_list[actual_index]
                if product > 85:
                    break
            if product == 85:
               valid_sublists.append(sublist)

    return valid_sublists
