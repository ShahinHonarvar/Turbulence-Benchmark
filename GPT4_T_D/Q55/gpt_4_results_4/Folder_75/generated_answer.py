
def lists_with_product_equal_n(circular_list):
    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    sublists = []
    size = len(circular_list)
    extended_list = circular_list * 2

    for start_index in range(size):
        for end_index in range(start_index + 1, start_index + size + 1):
            sublist = extended_list[start_index:end_index]
            if get_product(sublist) == 13:
                sublists.append(sublist)
    return sublists
