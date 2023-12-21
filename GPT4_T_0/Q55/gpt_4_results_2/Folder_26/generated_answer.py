
def lists_with_product_equal_n(circular_list):
    n = 93
    sublists = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i, length):
            sublist = circular_list[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                sublists.append(sublist)
        sublist = circular_list[i:] + circular_list[:i]
        product = 1
        for num in sublist:
            product *= num
        if product == n:
            sublists.append(sublist)
    return sublists
