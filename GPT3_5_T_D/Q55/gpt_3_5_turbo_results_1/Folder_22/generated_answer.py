
def lists_with_product_equal_n(circular_list):
    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    sublists = []
    size = len(circular_list)

    for i in range(size):
        for j in range(i, size):
            sublist = circular_list[i:j+1]
            if product_of_sublist(sublist) == 4:
                sublists.append(sublist)

    return sublists
