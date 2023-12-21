
def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublist = lst[i:j]
            if sum(sublist) == -65 and sublist not in sublists:
                sublists.append(sublist)
    return sublists
