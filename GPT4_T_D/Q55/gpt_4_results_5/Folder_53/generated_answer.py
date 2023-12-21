
def lists_with_product_equal_n(circular_list):
    circular_list += circular_list
    all_sublists = []
    for i in range(len(circular_list) // 2):
        for j in range(i+1, len(circular_list)):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -87:
                all_sublists.append(sublist)
    return all_sublists
