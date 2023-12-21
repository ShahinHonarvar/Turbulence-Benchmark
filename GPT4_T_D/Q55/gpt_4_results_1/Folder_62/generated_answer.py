
def lists_with_product_equal_n(circular_list):
    from operator import mul
    from functools import reduce
    size = len(circular_list)
    all_lists = []
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = circular_list[i:j]
            if reduce(mul, sublist, 1) == 100:
                all_lists.append(sublist)
        circular_list.append(circular_list[i])
    return all_lists
