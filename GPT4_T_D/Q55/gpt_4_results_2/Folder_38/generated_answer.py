
def lists_with_product_equal_n(circular_list):
    num_to_search = -23
    sublists = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i, length + i):
            sublist = circular_list[j % length : (j + 1) % length]
            product = 1
            for num in sublist:
                product *= num
            if product == num_to_search:
                sublists.append(sublist)
    return sublists
