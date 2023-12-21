
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    target = 851

    for i in range(size):
        for j in range(i, size + i):
            sublist = circular_list[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == target:
                sublists.append(sublist)

    return sublists
