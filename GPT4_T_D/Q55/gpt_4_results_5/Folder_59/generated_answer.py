
def lists_with_product_equal_n(lst):
    all_sublists = []
    len_list = len(lst)

    # get all possible sublists
    for sublist_len in range(2, len_list+1):
        for i in range(len_list):
            sublist = lst[i: i+sublist_len]
            if len(sublist) < sublist_len:
                sublist = sublist + lst[0: sublist_len - len(sublist)]
            all_sublists.append(sublist)

    # filter sublists where the product of its elements equals -3
    result = []
    for sublist in all_sublists:
        product = 1
        for num in sublist:
            product *= num
        if product == -3:
            result.append(sublist)

    return result
