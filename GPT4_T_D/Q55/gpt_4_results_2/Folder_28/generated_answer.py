
def lists_with_product_equal_n(circular_list):
    num_elements = len(circular_list)
    extended_circular_list = circular_list * 2
    valid_sublists = []
    for i in range(num_elements):
        for j in range(i+1, i+num_elements+1):
            sublist = extended_circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 85:
                valid_sublists.append(sublist)
    return valid_sublists
