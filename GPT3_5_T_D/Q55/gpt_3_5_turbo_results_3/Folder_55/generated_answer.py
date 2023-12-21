
def lists_with_product_equal_n(lst):
    def get_sublists(lst, size):
        n = len(lst)
        sublists = []
        for i in range(n):
            sublist = []
            for j in range(size):
                sublist.append(lst[(i + j) % n])
            sublists.append(sublist)
        return sublists

    sublists = []
    for size in range(1, len(lst) + 1):
        sublists.extend(get_sublists(lst, size))

    result = []
    for sublist in sublists:
        product = 1
        for num in sublist:
            product *= num
        if product == -6:
            result.append(sublist)

    return result
