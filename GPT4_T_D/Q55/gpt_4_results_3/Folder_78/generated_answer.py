
def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    matched_sublists = []
    circular_list.extend(circular_list)
    for i in range(size):
        for j in range(i+1, size+i+1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 74:
                matched_sublists.append(sublist)
    return matched_sublists
