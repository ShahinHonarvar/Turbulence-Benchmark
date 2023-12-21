
def lists_with_product_equal_n(circular_list):
    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i+1, n+1):
            sublist = circular_list[i:j]
            product = get_product(sublist)
            if product == 99:
                sublists.append(sublist)
    return sublists
