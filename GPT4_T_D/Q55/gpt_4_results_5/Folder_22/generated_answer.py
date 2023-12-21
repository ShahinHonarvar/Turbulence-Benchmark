
def lists_with_product_equal_n(lst):
    if not lst:
        return []
    lst = lst + lst
    len_list = len(lst)//2
    result_lists = []
    for i in range(len_list):
        for j in range(i+1, i + len_list + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 4:
                result_lists.append(sublist)
    return result_lists
