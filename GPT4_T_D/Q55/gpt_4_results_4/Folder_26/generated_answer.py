
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    sublist_of_93 = []
    # iterate over the circular list, taking the modulus to account for the circular nature
    for start_index in range(length):
        for sublist_len in range(1, length + 1):
            sublist = [circular_list[(start_index + i) % length] for i in range(sublist_len)]
            product = 1
            for num in sublist:
                product *= num
            if product == 93:
                sublist_of_93.append(sublist)
    return sublist_of_93
