
def lists_with_product_equal_n(lst):
    from itertools import combinations
    circular_lst = lst + lst
    sublists = []
    length = len(lst)
    for i in range(length*2):
        for j in range(i+1,length+i+1):
            sublist = circular_lst[i:j]
            product = 1
            for f in sublist:
                product *= f
            if product == 29:
                sublists.append(sublist)
    return sublists
