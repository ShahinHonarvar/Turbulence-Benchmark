
def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        current_sublist = [circular_list[i]]
        product = circular_list[i]
        for j in range(1, len(circular_list)):
            if product * circular_list[(i + j) % len(circular_list)] == 74:
                current_sublist.append(circular_list[(i + j) % len(circular_list)])
                sublists.append(current_sublist)
    return sublists
