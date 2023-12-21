
def lists_with_product_equal_n(circular_list):
    sublists = []
    size = len(circular_list)
    double_list = circular_list + circular_list
    for x in range(size):
        for y in range(x+1, x+size+1):
            sublist = double_list[x:y]
            product = 1
            for number in sublist:
                product *= number
            if product == 2:
                sublists.append(sublist)
    return sublists
