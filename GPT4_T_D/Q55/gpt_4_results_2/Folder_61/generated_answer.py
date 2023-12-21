
def lists_with_product_equal_n(circular_list):
    list_of_sublists = []
    n = len(circular_list)
    circular_list += circular_list
    for start_index in range(n):
        for end_index in range(start_index + 1, start_index + n + 1):
            sublist = circular_list[start_index:end_index]
            product = 1
            for number in sublist:
                product *= number
            if product == -10:
                list_of_sublists.append(sublist)
    return list_of_sublists
