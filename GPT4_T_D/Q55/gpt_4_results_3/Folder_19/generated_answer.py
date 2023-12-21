
def lists_with_product_equal_n(circular_list):
    output_lists = []
    circular_list = circular_list * 2
    for sublist_size in range(1, len(circular_list) // 2 + 1):
        for i in range(len(circular_list) // 2):
            sublist = circular_list[i:i+sublist_size]
            product = 1
            for number in sublist:
                product *= number
            if product == -54:
                output_lists.append(sublist)
    return output_lists
