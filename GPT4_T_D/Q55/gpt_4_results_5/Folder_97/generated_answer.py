
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for sublist_size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i: i + sublist_size]
            if i + sublist_size > n:
                sublist.extend(lst[0: (i + sublist_size) % n])
            product = 1
            for num in sublist:
                product *= num
            if product == -938:
                sublists.append(sublist)
    return sublists
