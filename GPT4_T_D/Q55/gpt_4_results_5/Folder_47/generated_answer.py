
def lists_with_product_equal_n(circular_list):
    circular_list = circular_list * 2
    sublist_list = []
    for window_size in range(1, len(circular_list)//2 + 1):
        for i in range(len(circular_list)):
            sublist = circular_list[i:i+window_size]
            product = 1
            for num in sublist:
                product *= num
            if product == -94:
                sublist_list.append(sublist)
    return sublist_list
