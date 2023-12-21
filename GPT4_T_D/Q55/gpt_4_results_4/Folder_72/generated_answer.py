
def lists_with_product_equal_n(circular_list):
    n = 10
    all_sublists = []
    list_size = len(circular_list)
    for i in range(list_size):
        for j in range(i,list_size):
            sublist = circular_list[i:j+1]
            product = 1
            for number in sublist:
                product *= number
            if product == n:
                all_sublists.append(sublist)
        circular_list.append(circular_list[i])
    return all_sublists
