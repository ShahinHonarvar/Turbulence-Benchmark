
def lists_with_product_equal_n(circular_list):
    circular_list = circular_list + circular_list[:-1]
    sublists = []
    for i in range(len(circular_list)-1):
        for j in range(i+1, len(circular_list)+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 537:
                sublists.append(sublist)
    return sublists
