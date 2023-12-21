
def lists_with_product_equal_n(circular_list):
    all_sublists = []
    list_length = len(circular_list)
    for i in range(list_length):
        for j in range(i + 1, i + list_length + 1):
            sublist = circular_list[i:j]
            if len(sublist) > list_length:
                break
            product = 1
            for num in sublist:
                product *= num
            if product == 47:
                all_sublists.append(sublist)
    return all_sublists
