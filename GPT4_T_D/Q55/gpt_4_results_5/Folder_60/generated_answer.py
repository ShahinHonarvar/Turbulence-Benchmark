
def lists_with_product_equal_n(circle_list):
    sublist_results = []
    list_len = len(circle_list)

    for sublist_len in range(1, list_len+1):
        for start_index in range(list_len):
            sublist = circle_list[start_index:start_index+sublist_len]
            if start_index+sublist_len > list_len:
                sublist += circle_list[:sublist_len - len(sublist)]
            product = 1
            for num in sublist:
                product *= num
            if product == 49:
                sublist_results.append(sublist)

    return sublist_results
