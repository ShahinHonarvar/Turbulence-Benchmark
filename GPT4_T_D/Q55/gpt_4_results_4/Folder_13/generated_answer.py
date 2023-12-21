
def lists_with_product_equal_n(list):
    from itertools import chain
    from operator import mul
    from functools import reduce
    double_list = list + list
    one_way_list = [double_list[i: j + 1] for i in range(len(list)) for j in range(i + 1, len(list))]
    all_lists = list(chain(*one_way_list))
    final_result = [item for item in all_lists if reduce(mul, item, 1) == 54]
    return final_result
