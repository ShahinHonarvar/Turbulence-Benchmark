
def lists_with_product_equal_n(circular_list):
    list_length = len(circular_list)
    sublists = []
    for i in range(list_length):
        for j in range(i+1, list_length + 1):
            sublist = circular_list[i:j] if j <= list_length else circular_list[i:] + circular_list[:j-list_length]
            product = 1
            for num in sublist:
                product *= num
            if product == -36:
                sublists.append(sublist)
    return sublists
