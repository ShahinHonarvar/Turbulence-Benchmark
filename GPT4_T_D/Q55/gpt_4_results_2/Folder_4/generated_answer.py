
def lists_with_product_equal_n(circular_list):
    list_size = len(circular_list)
    sublists = []
    for sublist_size in range(1, list_size + 1):
        for start_index in range(list_size):
            sublist = []
            for i in range(start_index, start_index + sublist_size):
                sublist.append(circular_list[i % list_size])
            if product_of_list(sublist) == 91:
                sublists.append(sublist)
    return sublists


def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product
