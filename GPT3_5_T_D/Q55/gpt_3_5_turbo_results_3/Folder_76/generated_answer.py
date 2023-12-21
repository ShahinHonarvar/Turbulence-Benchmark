
def lists_with_product_equal_n(circular_list):
    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            product = get_product(circular_list[i:j+1])
            if product == 247:
                sublists.append(circular_list[i:j+1])

    return sublists
